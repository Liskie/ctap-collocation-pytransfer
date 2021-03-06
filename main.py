# -*- coding:UTF-8 -*-
from utils_text import *
from syntactic import getSyntacticIndices

import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str)
    args = parser.parse_args()

    text = args.text

    example_text = "学习汉语的苦与乐我是一个生长于马来西亚的华裔，汉语对我来说，可以说是我的母语。" \
                   "但是因为当地政府所实行的教育政策和制度，我自始是以把汉语当作是第二与语文来学习，而经历了许多的苦与乐。" \
                   "在学校学习时，因当时的主要语言为英语，其次为当地的马来语，然后才是汉语。" \
                   "汉语的学习时间也受到限制。" \
                   "从另一角度来看，汉语的重要性也因社会的结构，尤其的通用程度只局限于华裔社会而不被国家重视。" \
                   "学习和应用汉语者会有被歧视和嘲笑的遭遇。" \
                   "我记得曾经因学习汉语而被不谙汉语的华裔老师劝告说汉语并无甚“实用价值”，应该放弃而专注于“实用”的其他语文。" \
                   "庆幸的是我当时没有接受那位老师的劝告。" \
                   "对于我来说，学习汉语的苦是经历人为的障碍，而不像其他的外国人因不是他们的母语而遇到了语文转换的困难。" \
                   "学习汉语的乐处可真多。" \
                   "在看国语电影时，能了解电影剧情和对白而不需靠字幕和翻译。" \
                   "和别人以汉语来交谈的亲切感等等。"

    text_dict = text_process(text)
    indices: dict = getSyntacticIndices(text_dict)
    for k, v in indices.items():
        print(f'{k}: {v}')
