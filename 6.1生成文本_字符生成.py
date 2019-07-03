
#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

import numpy as np
from keras.utils.vis_utils import plot_model

fin =open('wonderland.txt','rb')
#去除断行，和非ASCII字符，预处理后放入text变量中
lines = []
for line in fin:
    line = line.strip().lower()
    line = line.decode('ascii','ignore')

    if len(line)==0:
        continue
    lines.append(line)

fin.close()
text = ' '.join(lines)

#字符级别的RNN，将字典设置为文中出现的字符，例子中有42个字符，
#因为要处理的是字符的索引，非字符本身，创建必要的查询表
chars = set([c for c in text])
nb_chars = len(chars)
char2index = dict((c,i) for i,c in enumerate(chars))
index2char = dict((i,c) for i,c in enumerate(chars) )

#创建输入和标签，通过step变量给出字符数目，这里为1，来步进遍历文本，
# 提取大小为SEQLEN变量定义值，这里为10，的文本段
#通过文本段来预测，文本段下一字符为标签字符，即为预测字符
SEQLEN =10
STEP =1

input_chars = []#一句话中连续的十个字符
label_chars = []#接下来的的一个字符
for i in range(0,len(text) -SEQLEN,STEP):
    input_chars.append(text[i:i+SEQLEN])
    label_chars.append(text[i+SEQLEN])


#把输入和标签文本向量化，RNN输入每行都对应了前面的一个输入文本，输入中共有SEQLEN个字符，
#字典大小是nb_chars给定，
#把输入字符表示成one_hot编码，大小为nb_chars 的向量，这样每一行输入就是一个大小为SEQLEN和nb_chars的张量，输出是一个单一的字符，我们将输出标签表示为一个nb_chars的one_hot编码向量
X = np.zeros((len(input_chars),SEQLEN,nb_chars),dtype=np.bool)
Y = np.zeros((len(input_chars),nb_chars),dtype=np.bool)

for i ,input_char in enumerate(input_chars):
    for j ,ch in enumerate(input_char):
        X[i,j,char2index[ch]] =1
    Y[i,char2index[label_chars[i]]]=1