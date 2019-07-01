#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
# SpatialDropout1D特定维度，如一列或者某行做dropout
from keras.layers.core import Dense, Dropout, SpatialDropout1D
from keras.layers.convolutional import Conv1D
from keras.layers.embeddings import Embedding
from keras.layers.pooling import GlobalAveragePooling1D
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
import collections

import matplotlib.pyplot as plt
import nltk
import numpy as np

seed = 42
np.random.seed(seed)

# Kaggle上UMICH SI650情感分类竞赛中的句子做分类

INPUT_FILE = 'umich-sentiment-train.txt'
VOCAB_SIZE = 5000  # 只考虑文本中前5000个词汇
EMBED_SIZE = 300  # 生成的词向量维度
NUM_FILTERS = 256  # 卷积层滤波器数目
NUM_WORDS = 3  # 每个滤波器大小
BATCH_SIZE = 64
NUM_EPOCHS = 20

# 读入输入句子，用预料中最常用词汇构建字典，然后用这个字典转换成索引列表
counter = collections.Counter()
fin = open(INPUT_FILE, 'r')
maxlen = 0
for line in fin:
    _, sent = line.strip().split('t')
    words = [x.lower() for x in nltk.word_tokenize(sent)]
    if len(words) > maxlen:
        maxlen = len(words)
    for word in words:
        counter[word] += 1

fin.close()

word2index = collections.defaultdict(int)
for wid, word in enumerate(counter.most_common(VOCAB_SIZE)):
    word2index[word[0]] = wid + 1
vocab_size = len(word2index) + 1
word2index = {v: k for k, v in word2index.items()}

# 我们使用空白来填充每个句子，让它们达到预先设定的长度，本例子中是使用最长句子的单词数量
# 使用Keras工具函数把标签转换成类别格式
# 这两步再各个 项目中也经常用到
xs, ys = [], []
fin = open(INPUT_FILE, 'rb')
for line in fin:
    label, sent = line.strip().split("t")
    ys.append(int(label))
    words = [x.lower() for x in nltk.word_tokenize(sent)]
    wids = [word2index[word] for word in words]
    xs.append(wids)
fin.close()
########*******************************************##################!!!!!!!!!!
X = pad_sequences(xs, maxlen=maxlen)
Y = np_utils.to_categorical(ys)
########*******************************************##################!!11111111

# 最后，按照70:30 的比例划分训练集合测试集，
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.3, random_state=seed)

#def layers
model = Sequential()
model.add(Embedding(vocab_size,EMBED_SIZE,input_length=max))
model.add(SpatialDropout1D(Dropout(0.2)))
model.add(Conv1D(filters=NUM_FILTERS,kernel_size=NUM_WORDS,activation='relu'))
model.add(GlobalAveragePooling1D())
model.add(Dense(2,activation='softmax'))



#编译模型
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
history = model.fit(Xtrain,Ytrain,batch_size=BATCH_SIZE,epochs=NUM_EPOCHS,validation_data=(Xtest,Ytest))

