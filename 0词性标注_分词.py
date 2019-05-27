#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

import jieba.posseg as pseg

strings = "小明硕士毕业于中国科学院计算所，后在日本京都大学深造"
seg_list = pseg.cut(strings)

print("\njieba词性标注: ")
for word, flat in seg_list:
    print("%s | %s" % (word, flat))
