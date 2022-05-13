notHV = ['的', '吗', '吧', '呢', '啊', '呀', '之', '等']
prepositions = ['把', '被', '对', '给', '跟', '将', '为', '向', '由', '与', '和', '同']


def getColl(words):
    collocation = []
    for key, value in words.items():
        parent_id = int(value['parent'])
        if parent_id == -1:
            continue
        parent_cont = words[parent_id]['cont'] #搭配词提取

        if value['pos'] in ['PU', 'FW'] or words[parent_id]['pos'] in ['PU', 'FW']:
            continue

        # P_X_DN
        if value['relate'] == 'case' and value['pos'] == 'LC':
            if key > parent_id and parent_id > 0 and words[parent_id-1]["relate"] == 'case':
                if words[parent_id-1]['pos'] == 'P' and words[parent_id-1]['cont']in ['在', '到', '从', '自', '自从',
                                        '向','往', '除了', '于', '沿着', '至','由', '顺着', '朝', '朝着', '沿','向着']:
                    coll_p_dn = words[parent_id-1]['cont'] + '\t' + 'X' + '\t' + value['cont'] + '\t' + 'P_X_DN'
                    collocation.append(coll_p_dn)
        if value['relate'] == 'case' and value['pos'] == 'P' and value['cont'] in ['在', '当', '每当', '从', '自从','自', 
                                                                                   '到']:
            if key < parent_id and words[parent_id]['cont'] in ['时', '时候']:
                coll_p_dn = value['cont'] + '\t' + 'X' + '\t' + words[parent_id]['cont'] + '\t' + 'P_X_DN'
                collocation.append(coll_p_dn)
            

        # P_X_U
        if value['relate'] in ['aux:asp', 'mark'] and value['pos'] == 'u' and value['cont'] not in notHV:
            if key > parent_id + 1 and words[parent_id]['pos'] == 'P':
                coll_p_u = parent_cont + '\t' + 'X' + '\t' + value['cont'] + '\t' + 'P_X_U'
                collocation.append(coll_p_u)

        # CN
        if value['relate'] == 'mark:clf' and value['pos'] == 'M':
            if words[parent_id]['pos'] in ['CD','DT'] and key > parent_id:
                parent_id2 = int(words[parent_id]['parent'])
                if words[parent_id]['relate'] == 'nummod' and key < parent_id2:
                    coll_q_n = value['cont'] + '\t' + words[parent_id2]['cont'] + '\t' + 'Q_N'
                    collocation.append(coll_q_n)
        # AN
        if value['relate'] == 'amod' and value['pos'] in ['VA', 'JJ']:
            if words[parent_id]['pos'] in ['NN', 'NR', 'NT', 'LC']:
                if key == parent_id - 1:
                    coll_a_n = value['cont'] + '\t' + parent_cont + '\t' + 'A_N'
                    collocation.append(coll_a_n)
                elif key == parent_id - 2 and words[parent_id - 1]['cont'] == '的':
                    coll_a_de_n = value['cont'] + '\t' + '的' + '\t' + parent_cont + '\t' + 'A_DE_N'
                    collocation.append(coll_a_de_n)
                elif words[key + 1]['cont'] == '的':
                    coll_a_de_x_n = value['cont'] + '\t' + '的' + '\t' + 'X' + '\t' + parent_cont + '\t' + 'A_DE_X_N'
                    collocation.append(coll_a_de_x_n)
                elif words[parent_id - 1]['cont'] == '的':
                    coll_a_x_de_n = value['cont'] + '\t' + 'X' + '\t' + '的' + '\t' + parent_cont + '\t' + 'A_X_DE_N'
                    collocation.append(coll_a_x_de_n)
                else:
                    coll_a_x_n = value['cont'] + '\t' + 'X' + '\t' + parent_cont + '\t' + 'A_X_N'
                    collocation.append(coll_a_x_n)

        # VO
        if value['relate'] == 'dobj' and value['pos'] in ['NN', 'NR', 'NT', 'LC']:
            if words.__contains__(parent_id + 1) and words[parent_id + 1]['relate'] in ['aux:asp', 'mark','advmod:rcomp','xcomp'] and \
                    words[parent_id + 1]['cont'] not in notHV:
                if words.__contains__(parent_id + 2) and words[parent_id + 2]['relate'] in ['aux:asp', 'mark','advmod:rcomp','xcomp'] and \
                        words[parent_id + 2]['cont'] not in notHV:
                    coll_v_2hv_o = parent_cont + '\t' + words[parent_id + 1]['cont'] + '\t' + words[parent_id + 2][
                        'cont'] + '\t' + value['cont'] + '\t' + 'V_2HV_O'
                    collocation.append(coll_v_2hv_o)
                else:
                    coll_v_hv_o = parent_cont + '\t' + words[parent_id + 1]['cont'] + '\t' + value[
                        'cont'] + '\t' + 'V_HV_O'
                    collocation.append(coll_v_hv_o)
            else:
                coll_v_o = parent_cont + '\t' + value['cont'] + '\t' + 'V_O'
                collocation.append(coll_v_o)
        if value['relate'] == 'cop' and value['pos'] in ['VV', 'VC', 'VE']:
            coll_v_o = value['cont'] + '\t' + parent_cont + '\t' + 'V_O'
            collocation.append(coll_v_o)


        # SP
        if value['relate'] in ['nsubj', 'nsubj:pass'] and value['pos'] not in ['PN', 'LC']:
            if words.__contains__(parent_id + 1) and words[parent_id + 1]['relate'] in ['aux:asp','mark','advmod:rcomp','xcomp'] and \
                    words[parent_id + 1]['cont'] not in notHV:
                if words.__contains__(parent_id + 2) and words[parent_id + 2]['relate'] in ['aux:asp', 'mark','advmod:rcomp','xcomp'] and \
                        words[parent_id + 2]['cont'] not in notHV:
                    coll_s_v_2hv = value['cont'] + '\t' + parent_cont + '\t' + words[parent_id + 1]['cont'] + '\t' + \
                                   words[parent_id + 2]['cont'] + '\t' + 'S_V_2HV'
                    collocation.append(coll_s_v_2hv)
                else:
                    coll_s_v_hv = value['cont'] + '\t' + parent_cont + '\t' + words[parent_id + 1][
                        'cont'] + '\t' + 'S_V_HV'
                    collocation.append(coll_s_v_hv)
            elif words[parent_id - 1]['cont'] not in [':', '：']:
                coll_s_v = value['cont'] + '\t' + parent_cont + '\t' + 'S_V'
                collocation.append(coll_s_v)

        # AP
        if value['relate'] in ['advmod','aux:modal','advmod:dvp','neg'] and value['pos'] in ['VA', 'JJ', 'AD', 'VV','VE','VC']:
            if key == parent_id - 1:
                if words[parent_id]['pos'] in ['VA', 'JJ']:
                    coll_d_a = value['cont'] + '\t' + parent_cont + '\t' + 'D_A'
                    collocation.append(coll_d_a)
                elif words[parent_id]['pos'] in ['VV','VE','VC']:
                    coll_d_v = value['cont'] + '\t' + parent_cont + '\t' + 'D_V'
                    collocation.append(coll_d_v)
            elif key < parent_id and words[key + 1]['cont'] == '地':
                coll_d_di_v = value['cont'] + '\t' + '地' + '\t' + parent_cont + '\t' + 'D_DI_V'
                collocation.append(coll_d_di_v)
            elif key < parent_id:
                if words[parent_id]['pos'] in ['VA', 'JJ']:
                    coll_d_x_a = value['cont'] + '\t' + 'X' + '\t' + parent_cont + '\t' + 'D_X_A'
                    collocation.append(coll_d_x_a)
                elif words[parent_id]['pos'] in ['VV','VC','VE']:
                    coll_d_x_v = value['cont'] + '\t' + 'X' + '\t' + parent_cont + '\t' + 'D_X_V'
                    collocation.append(coll_d_x_v)

        # PV
        if value['pos'] in ['BA','SB','LB'] and value['cont'] in prepositions:
            if value['relate'] in ['aux:ba','aux:pass'] and words[parent_id]['pos'] in ['VV','VC','VE'] and key < parent_id:
                if words.__contains__(parent_id + 1) and words.__contains__(parent_id + 2) and words[parent_id + 1][
                    'relate'] in ['aux:asp', 'mark','advmod:rcomp','xcomp'] and words[parent_id + 1]['cont'] not in notHV and words[parent_id + 2][
                    'relate'] in ['aux:asp', 'mark','advmod:rcomp','xcomp'] and words[parent_id + 2]['cont'] not in notHV:
                    coll_p_v_2hv = value['cont'] + '\t' + 'X' + '\t' + parent_cont + '\t' + words[parent_id + 1][
                        'cont'] + '\t' + words[parent_id + 2]['cont'] + '\t' + 'P_X_V_2HV'
                    collocation.append(coll_p_v_2hv)
                elif words.__contains__(parent_id + 1) and words[parent_id + 1]['relate'] in ['aux:asp', 'mark','advmod:rcomp','xcomp'] and \
                        words[parent_id + 1]['cont'] not in notHV:
                    coll_p_v_hv = value['cont'] + '\t' + 'X' + '\t' + parent_cont + '\t' + words[parent_id + 1][
                        'cont'] + '\t' + 'P_X_V_HV'
                    collocation.append(coll_p_v_hv)
                else:
                    coll_p_v = value['cont'] + '\t' + 'X' + '\t' + parent_cont + '\t' + 'P_X_V'
                    collocation.append(coll_p_v)
        if value['pos'] == 'P' and value['cont'] in prepositions:
            if value['relate'] == 'case' and words[parent_id]['pos'] in ['NN','NR','PN'] and key < parent_id:
                parent_two = int(words[parent_id]['parent'])
                if words[parent_id]['relate'] in ['nmod:prep'] and parent_id < parent_two and words[parent_two]['pos'] in ['VV','VC','VE']:
                    if words.__contains__(parent_two + 1) and words.__contains__(parent_two + 2) and words[parent_two + 1][
                    'relate'] in ['aux:asp', 'mark','advmod:rcomp','xcomp'] and words[parent_two + 1]['cont'] not in notHV and words[parent_two + 2][
                    'relate'] in ['aux:asp', 'mark','advmod:rcomp','xcomp'] and words[parent_two + 2]['cont'] not in notHV:
                        coll_p_v_2hv = value['cont'] + '\t' + 'X' + '\t' + words[parent_two]['cont'] + '\t' + words[parent_two + 1][
                        'cont'] + '\t' + words[parent_two + 2]['cont'] + '\t' + 'P_X_V_2HV'
                        collocation.append(coll_p_v_2hv)
                    elif words.__contains__(parent_two + 1) and words[parent_two + 1]['relate'] in ['aux:asp', 'mark','advmod:rcomp','xcomp'] and \
                        words[parent_two + 1]['cont'] not in notHV:
                        coll_p_v_hv = value['cont'] + '\t' + 'X' + '\t' + words[parent_two]['cont'] + '\t' + words[parent_two + 1][
                        'cont'] + '\t' + 'P_X_V_HV'
                        collocation.append(coll_p_v_hv)
                    else:
                        coll_p_v = value['cont'] + '\t' + 'X' + '\t' + parent_cont + '\t' + 'P_X_V'
                        collocation.append(coll_p_v)
                        
        # PC
        if value['relate'] in ['advmod:rcomp','xcomp']:
            if key == parent_id + 1:
                if words.__contains__(key + 1):
                    if words[key + 1]['cont'] in ['了', '得', '过']:
                        coll_v_c_u = parent_cont + '\t' + value['cont'] + '\t' + words[key + 1]['cont'] + '\t' + 'V_C_U'
                        collocation.append(coll_v_c_u)
                    else:
                        coll_v_c = parent_cont + '\t' + value['cont'] + '\t' + 'V_C'
                        collocation.append(coll_v_c)
            elif key == parent_id + 2:
                if words[key - 1]['cont'] in ['了', '得', '过']:
                    coll_v_u_c = parent_cont + '\t' + words[key - 1]['cont'] + '\t' + value['cont'] + '\t' + 'V_U_C'
                    collocation.append(coll_v_u_c)
                elif words[key - 1]['relate'] == 'advmod':
                    coll_v_d_c = parent_cont + '\t' + words[key - 1]['cont'] + '\t' + value['cont'] + '\t' + 'V_D_C'
                    collocation.append(coll_v_d_c)
                elif words[key - 1]['relate'] == 'amod':
                    if words[key - 1]['pos'] in ['CD', 'OD']:
                        coll_v_m_c = parent_cont + '\t' + 'm' + '\t' + value['cont'] + '\t' + 'V_M_C'
                        collocation.append(coll_v_m_c)
                    else:
                        coll_v_a_c = parent_cont + '\t' + 'A' + '\t' + value['cont'] + '\t' + 'V_A_C'
                        collocation.append(coll_v_a_c)
            elif key > parent_id + 2:
                if words[parent_id + 1]['cont'] in ['了', '得', '过']:
                    if key == parent_id + 3:
                        if words[key - 1]['relate'] == 'amod':
                            if words[key - 1]['pos'] in ['CD', 'OD']:
                                coll_v_u_m_c = parent_cont + '\t' + words[key - 2]['cont'] + '\t' + 'm' + '\t' + value[
                                    'cont'] + '\t' + 'V_U_M_C'
                                collocation.append(coll_v_u_m_c)
                            else:
                                coll_v_u_a_c = parent_cont + '\t' + words[key - 2]['cont'] + '\t' + words[key - 1][
                                    'cont'] + '\t' + value['cont'] + '\t' + 'V_U_A_C'
                                collocation.append(coll_v_u_a_c)
                        elif words[key - 1]['relate'] == 'advmod':
                            if value['pos'] not in ['VV','VC','VE']:
                                coll_v_u_d_c = parent_cont + '\t' + words[key - 2]['cont'] + '\t' + words[key - 1][
                                    'cont'] + '\t' + value['cont'] + '\t' + 'V_U_D_C'
                                collocation.append(coll_v_u_d_c)
                            elif words[key + 1]['pos'] == 'PU':
                                coll_v_u_d_c = parent_cont + '\t' + words[key - 2]['cont'] + '\t' + words[key - 1][
                                    'cont'] + '\t' + value['cont'] + '\t' + 'V_U_D_C'
                                collocation.append(coll_v_u_d_c)
                        else:
                            coll_v_u_x_c = parent_cont + '\t' + words[key - 2]['cont'] + '\t' + 'X' + '\t' + value[
                                'cont'] + '\t' + 'V_U_X_C'
                            collocation.append(coll_v_u_x_c)
                    else:
                        coll_v_u_x_c = parent_cont + '\t' + words[parent_id + 1]['cont'] + '\t' + 'X' + '\t' + value[
                            'cont'] + '\t' + 'V_U_X_C'
                        collocation.append(coll_v_u_x_c)
                else:
                    coll_v_x_c = parent_cont + '\t' + 'X' + '\t' + value['cont'] + '\t' + 'V_X_C'
                    collocation.append(coll_v_x_c)
    return collocation

coll_dict = {"V_O": "VO", "V_HV_O": "VO", "V_2HV_O": "VO", "D_V": "AP",
             "S_V_HV": "SP", "P_X_DN": "PP*", "V_C": "PC*",
             "S_V": "SP", "D_A": "AP", "Q_N": "CN*", "V_D_C": "PC*", "P_X_U": "PP*",
             "P_X_V": "PV*", "A_N": "AN", "A_X_DE_N": "AN", "D_X_A": "AP", "P_X_V_HV": "PV*",
             "D_X_V": "AP", "V_U_C": "PC*", "A_DE_N": "AN", "V_X_C": "PC*",
             "V_C_U": "PC*", "D_DI_V": "AP", "V_U_X_C": "PC*", "V_M_C": "PC*", "V_U_A_C": "PC*",
             "A_X_N": "AN", "V_U_D_C": "PC*", "V_U_M_C": "PC*", "A_DE_X_N": "AN",
             "P_X_V_2HV": "PV*", "S_V_2HV": "SP", "V_A_C": "PC*"}


def isUniqueColl(coll):
    typ = coll_dict[coll.split('\t')[-1]]
    if typ in ['PC*', 'PV*', 'CN*', 'PP*']:
        return True
    else:
        return False

# 指定了encoding参数
with open('low_freq_coll.txt', 'r', encoding="utf8") as coll_params:
    lowfreq_colls = {line.strip():0 for line in coll_params}

def isLowFreqColl(coll):
    if coll in lowfreq_colls:
        return True
    return False