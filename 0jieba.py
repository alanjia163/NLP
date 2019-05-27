#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
'''
jieba三种分词模式
注意jieba分词后得到的是一个list
'''

import jieba
import jieba.posseg as pseg

# 1. print("\n jieba分词全模式")
seg_list = jieba.cut("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", cut_all=True)
print("Full    Mode:", "/".join(seg_list))
# 2. print("\n jieba分词精确模式")
seg_list1 = jieba.cut("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", cut_all=False)  ## cut_all不写也行,默认是精确模式
print('Default Mode:', '/'.join(seg_list1))
# 3. print("\n搜索引擎模式:")
seg_list2 = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
print("Search  Mode:", '/'.join(seg_list2))
