#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin


import jieba,re
from 3.4词性标注  import seg_sentences

with open("test.txt",'r',encoding='utf8') as  f,open("out.txt",'w',encoding='utf8') as fout:
    for line in f:
        line = line.strip()
        if len(line>0):
            fout.write(' '.join(seg_sentences(line))+"\n")

