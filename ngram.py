# -*- coding:utf-8 -*-
# Author: Jia ShiLin

import json,re
import numpy
import pandas as pd

import numpy as np
import itertools
from itertools import chain
from tokenizer import seg_sentences
pattern = re.compile(u'[^a-zA-Z\u4E00-\u9FA5]')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,numpy.integer):
            return float(obj)
        elif isinstance(obj,numpy.floating):
            return float(obj)
        elif isinstance(obj,numpy.ndarray):
            return float(obj)
        return json.JSONEncoder.default(self,obj)
def _replace_c(text)
    intab = ",?!"
    outtab = "，？！"
    deltab = ")(+_-.>< "
    trantab=text.maketrans(intab, outtab,deltab)
    return text.translate(trantab)


# def remove_phase(phase_list):
#     remove_phase="aa,ab,abc,ad,ao,az,a写字楼,a区,a地块,a客户,a施工方,a系列,a项目,a系统"
#     remove_phase_set=set(remove_phase.split(","))
#     phase_list_set=set(phase_list)
#     phase_list_set.difference(remove_phase_set)
#     return list(phase_list_set)


def generate_ngram(sentence,n=4,m=2):
    if len(sentence)<n:
        n = len(sentence)

    temp = [tuple(sentence[i - k :i]) for k in range(m,n+1) for i in range(k,len(sentence)+1)]
    return [item for item in temp if len(''.join(item).strip())> and len(pattern.findall(''.join(item).strip())) ==0]


if __name__ == '__main__':
    #分词进行n-gram
    copus_character = [generate_ngram(line.strip(),with_filter=True) for line in open('text.txt','r',encoding='utf8')
                                      if len(line.strip())>0 and "RESUMEDOCSSTARTFLAG" not in line]

    #先用hanlp进行分词，在对词进行n-gram
    copus_word = [generate_ngram(seg_sentences(line.strip(),with_filter=True) ) for line  in open('text.txt','r',encoding='utf8')
                  if len(line.strip())>0 and "RESUMEDOCSSTARTFLAG" not in line])]

    copus_word = chain.from_iterable(copus_word)
    copus_word = ['_'.join(item) for item in copus_word ]
    fout = open("ngram2_3.txt", "w", encoding='utf-8')

    dic_filter={}                     # 统计词频
    for item in copus_word:
        if item in dic_filter:
            dic_filter[item]+=1
        else:
            dic_filter[item]=1
    sort_dic=dict(sorted(dic_filter.items(),key=lambda val:val[1],reverse=True))       #reverse=True为降序排列,返回list
    fout.write(json.dumps(sort_dic, ensure_ascii=False,cls=NumpyEncoder))#
    '''
    json.dumps()和json.loads()是json格式处理函数（可以这么理解，json是字符串）
　　(1)json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
　　(2)json.loads()函数是将json格式数据转换为字典（可以这么理解，json.loads()函数是将字符串转化为字典）
`   '''
    fout.close()


















