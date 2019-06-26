#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
'''
窗口大小为1，只中心词左右紧邻的上下文的取词数
'''
from keras.layers import merge
from keras.layers.core import Dense,Reshape
from  keras.layers.embeddings import Embedding
from keras.models import Sequential



vocab_size = 5000#假定词典大小为5000
embed_size = 300

#为中心词创建一个序贯模型，模型的输出是词在字典中的ID，向量权重的初始值设为很小的随机值，
#通过反向传播算法来更新这些权重，下一层把输入形状变为embed_size大小
word_model = Sequential()
word_model.add(Embedding(vocab_size,embed_size,embeddings_initializer=='glorot_uniform',input_length=1))
word_model.add(Reshape((embed_size,)))

