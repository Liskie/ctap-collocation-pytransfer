from math import sqrt
from utils_coll import *


def getSyntacticIndices(text_dict):
    indices = {}

    # get linguistic features
    collocation_list = []

    for sent_id, info in text_dict.items():
        sent, worddict = info['sent'], info['worddict']
        collocations = getColl(worddict)
        collocation_list.extend(collocations)


    # update collocation based indices
    if len(collocation_list) > 10:
        coll_num = len(collocation_list)
        sqrt_coll_num = sqrt(coll_num)

        set_colls = set(collocation_list)
        if len(set_colls) > 0:
            coll_diversity = len(set_colls) / sqrt_coll_num
            indices['TOTAL_RTTR'] = coll_diversity
        else:
            indices['TOTAL_RTTR'] = 0.

        unique_colls = [coll for coll in collocation_list if isUniqueColl(coll)]
        if len(set(unique_colls)) > 0:
            indices['UNIQUE_RTTR'] = len(set(unique_colls)) / (sqrt(len(unique_colls)) + 1)
        else:
            indices['UNIQUE_RTTR'] = 0.
        if len(unique_colls) > 0:
            indices['UNIQUE_RATIO'] = len(unique_colls) / coll_num
        else:
            indices['UNIQUE_RATIO'] = 0.

        lowfreq_collls = [coll for coll in collocation_list if isLowFreqColl(coll)]
        if len(lowfreq_collls) > 0:
            indices['LOWFREQ_RATIO'] = len(lowfreq_collls) / coll_num
        else:
            indices['LOWFREQ_RATIO'] = 0.

        # coll indices based on different types
        # coll_types = ['VO', 'SP', 'AN', 'AP', 'CN*', 'PP*', 'PV*', 'PC*']
        # coll_type_dict = {k: [] for k in coll_types}
        #
        # for coll in collocation_list:
        #     typ = coll_dict[coll.split('\t')[-1]]
        #     coll_type_dict[typ].append(coll)
        #
        # for ct, v in coll_type_dict.items():
        #     indices[ct + '_RATIO'] = len(v) / len(collocation_list)
        #     indices[ct + '_RTTR'] = 0
        #     if v:
        #         indices[ct + '_RTTR'] = len(set(v)) / sqrt(len(v))

    return indices
