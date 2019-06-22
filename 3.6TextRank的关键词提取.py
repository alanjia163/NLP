#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

from jieba import analyse

# 引入关键词提取接口
textrank = analyse.textrank  #

# 原始文本
path = 'TextRank.txt'
with open(path, ) as f:
    text = str(f.read())
    print('\nkeywords by textrank:')  # 基于TextRank算法进行关键词提取


    #可以到定义的系统textrank.py原函数中修改默然值，查看值，topK表示最高多少个词了列出，allowPOS表示允许保留的词性词
    ##  def textrank(self, sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'), withFlag=False):
    keywords = textrank(text,topK=10,withWeight=True,allowPOS=('n','a','ns'))

    #输出提取出的关键词 f
    words = [keywords for keywords,w in keywords if w >0.2]
    print(' '.join(words)+'\n')