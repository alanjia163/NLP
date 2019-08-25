#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Jia ShiLin
if __name__ == '__main__':
    # inp = input()
    # # inp ='123,456'
    # num1 = inp.split(',')[0]
    # num2 = inp.split(',')[1]
    # sum1 =0
    # for i in num1:
    #     sum1=int(i)*int(num2)+sum1*10
    # print(sum1)
    num1 ='123'
    num2 ='456'
    num3 =123*456
    print(num3)
    sum1 = 0

    sum2 = 0
    for i in num1:

        for j in num2:
            sum1 = int(i) * int(j) + sum1 * 10
        sum2 = sum2*10 + sum1
        sum1=0
    print(sum2)
    # return str(sum2)