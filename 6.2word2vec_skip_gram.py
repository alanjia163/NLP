#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin


import collections
import math
import os

import random
import zipfile
import numpy as np
from six.moves import urllib, xrange

import tensorflow as tf

# data
filename = 'text8.zip'


# read_data
def read_data(filename):
    with zipfile.ZipFile(filename) as f:
        data = tf.compat.as_str(f.read(f.namelist()[0])).spit()
    return data


words = read_data(filename)


# step1提出高频停用词减少模型噪音,加速训练
def remove_fre_stop_word(words):
    t = 1e-5
    threshold = 0.8  # 剔除概率阈值
    # 统计单词频率
    int_word_counts = collections.Counter(words)
    total_count = len(words)
    # 计算单词频率
    word_freqs = {w: c / total_count for w, c in int_word_counts.items()}
    # 计算被剔除的概率
    prob_drop = {w: 1 - np.sqrt(t / f) for w, f in word_freqs.items()}
    # 对单词进行采样
    train_words = [w for w in words if prob_drop[w] < threshold]
    return train_words


words = remove_fre_stop_word(words)

# step 2 Build the dictionary and replace rare words with UKN  koken
# vocabulary_size  = len(words)
vocabulary_size = len(set(words))  # words中不重复的分词数量
print('Data size', vocabulary_size)
def build_dataset(words):
    count = [['UKN',-1]]
    #collections.Couter(words).most+common

    #words中每个分词计数，然后按照词频降序排列放在count里：[['UNK', -1], ('的', 99229), ('在', 25925), ('是', 20172), ('年', 17007), ('和', 16514), ('为', 15231), ('了', 13053), ('有', 11253), ('与', 11194)]
    count.extent(collections.Counter(words).most_common(vocabulary_size-1))
    dictionary = dict()
    # count中每个词分配一个编号，：[('UNK', 0), ('的', 1), ('在', 2), ('是', 3), ('年', 4), ('和', 5), ('为', 6), ('了', 7), ('有', 8), ('与', 9)]
    for word , _ in count:

        dictionary[word] = len(dictionary)
    data =list()
    unk_count = 0
    data = [dictionary[word] if word in dictionary else 0 for  word in  words]
    count[0][1] = unk_count
    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))     # 将dictionary中的key和value对换:[(0, 'UNK'), (1, '的'), (2, '在'), (3, '是'), (4, '年'), (5, '和'), (6, '为'), (7, '了'), (8, '有'), (9, '与')]
                                                                               # 相当于key是编号，value是对应的词
    return data, count, dictionary, reverse_dictionary


data, count, dictionary, reverse_dictionary = build_dataset(words)             # data：2262896,语料中的每个词的对应的编号； count:199247，相当于词频表，key是语料中所有的词，value是词频；
                                                                               # dictionary：199247，这个语料对应的词典，key是词，value是唯一编号； reverse_dictionary：199247，这个语料对应的词典，key是唯一编号，value是词；
del words  # Hint to reduce memory.
print('Most common words (+UNK)', count[:5])
print('Sample data', data[:10], [reverse_dictionary[i] for i in data[:10]])

data_index = 0

