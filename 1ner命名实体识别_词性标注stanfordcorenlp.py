#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
'''
需要下载俩个相应的工具包
'''
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r"NLP/stanfordnlp/", lang='zh')

# 读入等待处理的文件
f_in = open("news.txt", 'r', encoding='utf8')

# 保存文件的写入准备
f_ner = open("ner.txt", "w", encoding="utf8")
f_tag = open("pos_tag.txt", "w", encoding="utf8")

for line in f_in:
    line = line.strip()
    if len(line) < 1:
        continue
    # 命名实体识别
    f_ner.write("".join([each[0] + "/" + each[1] for each in nlp.ner(line) if len(each) == 2]) + "\n")
    # 词性标注
    f_tag.write("".join([each[0] + "/" + each[1] for each in nlp.pos_tag(line) if len(each) == 2]) + "\n")
f_ner.close()
f_tag.close()
print("完成")

"""
sentence = '清华大学位于北京。' 

print (nlp.word_tokenize(sentence)) 
print (nlp.pos_tag(sentence)) 
print (nlp.ner(sentence)) 
print (nlp.parse(sentence)) 
print (nlp.dependency_parse(sentence))

"""
