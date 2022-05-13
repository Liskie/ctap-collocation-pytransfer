import re
from corenlp_client import CoreNLP
from corenlp_client.__corenlp_client import Annotation


def text_process(text):
    annotator = CoreNLP(url="https://corenlp.run", lang="zh")
    paras = text.strip().split("\n")
    text_dict = {}
    sent_id = 1

    for para in paras:
        para = para.strip()
        if len(para) < 3:
            continue

        params_annotators = ','.join(["tokenize", "ssplit", "pos", "parse", "depparse"])
        anno_res = annotator._request_corenlp(para, params_annotators)
        para_anno = Annotation(anno_res)

        for sent_tokens, sent_deps in zip(para_anno.tokens, para_anno.basic_dep):
            sent = " ".join([word["word"] for word in sent_tokens])
            sent = re.sub("(?<![A-Za-z0-9]) (?![A-Za-z0-9])", "", sent)
            if len(sent) < 3:
                continue
            sent_anno_dict = {"worddict": {}, "sent": sent}
            for token_id, (token, dep) in enumerate(zip(sent_tokens, sent_deps)):
                token_dict = {
                    "cont": token["word"],
                    "pos": token["pos"],
                    "parent": int(dep["governor"]) - 1,
                    "relate": dep["dep"]
                }
                sent_anno_dict["worddict"][token_id] = token_dict
            text_dict[sent_id] = sent_anno_dict
            sent_id += 1
    annotator.close()
    return text_dict
