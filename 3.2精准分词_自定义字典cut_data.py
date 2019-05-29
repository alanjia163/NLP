#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin

import jieba
import re
#from tokenizer import cut_hanlp

# 加载自定义字典
jieba.load_userdict("3dict.txt")


def merge_two_list(a, b):
    '''
        c = merge_two_list(["你好","很好","非常好"],["abc","ade","abcd","abc",'efg']
        ----> c = ['你好', 'abc', '很好', 'ade', '非常好', 'abcd', 'abc', 'efg']
    :param a:
    :param b:
    :return: c
    '''
    # 传入两个list,将b中元素分别从a[i]位置插入到a中,
    c = []
    len_a, len_b = len(a), len(b)
    minlen = min(len_a, len_b)
    for i in range(minlen):
        c.append(a[i])
        c.append(b[i])

    if len_a > len_b:
        for i in range(minlen, len_a):
            c.append(a[i])
    else:
        for i in range(minlen, len_b):
            c.append(b[i])
    return c


if __name__ == '__main__':
    # data
    file_open = open("text.txt", "r", encoding="utf8")
    file_save = open("result_cut.txt", "w", encoding="utf8")

    # 添加正则匹配规则
    regex1 = u'(?:[^\u4e00-\u9fa5（）*&……%￥$，,。.@! ！]){1,5}期'  # 非汉字xxx期
    regex2 = r'(?:[0-9]{1,3}[.]?[0-9]{1,3})%'  # xx.xx%
    # 正则对象
    p1 = re.compile(regex1)
    p2 = re.compile(regex2)
    # 对每一行进行p1和p2判断
    for line in file_open.readlines():

        # 第一个regex1的匹配操作
        result1 = p1.findall(line)  # 返回匹配到的list
        if result1:
            regex_re1 = result1
            line = p1.sub("FLAG1", line)  # 将匹配到的替换成FLAG1

        # 第二个regex2的匹配操作
        result2 = p2.findall(line)
        if result2:
            line = p2.sub("FLAG2", line)

        # 分词操作
        words = jieba.cut(line)  # 结巴分词，返回一个generator object
        result = " ".join(words)  # 结巴分词结果 本身是一个generator object，所以使用 “ ”.join() 拼接起来

        if "FLAG1" in result:
            result = result.split("FLAG1")
            result = merge_two_list(result, result1)
            ss = result
            result = "".join(result)  # 本身是个list，我们需要的是str，所以使用 "".join() 拼接起来

        if "FLAG2" in result:
            result = result.split("FLAG2")
            result = merge_two_list(result, result2)
            result = "".join(result)

        file_save.write("jieba_save:"+result)
    file_save.close() #一定!一定!要加这一句否则不能写入文件