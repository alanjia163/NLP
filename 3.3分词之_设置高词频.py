#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

import jieba
import os


jieba.load_userdict("dict.txt")
fp =open("dict.txt",'r',encoding='utf8')
for line in fp:
    line = line.strip()
    jieba.suggest_freq(line,tune=True)


if __name__ == '__main__':

    file = open("news.txt",'r',encoding="utf8")

    for line in file:
        if len(line.strip())>=1:
            word_jieba =''.join(jieba.cut(line) )
            print("words_jieba:" + word_jieba)

    file.close()
