# !/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import importlib
import jieba
import jieba.posseg


if __name__ == "__main__":
    importlib.reload(sys)
    f = open('.\\24.novel.txt', encoding='utf-8')
    str = f.read()
    f.close()

    seg = jieba.posseg.cut(str)
    for s in seg:
        print(s.word, s.flag, '|',)
        # print(s.word, '|',)
