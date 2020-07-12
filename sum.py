# coding: utf-8

# @Time   : 2020/7/10 11:00
# @Author : Liu rucai
# @Software  : PyCharm
import random
import pandas as pd
import numpy as np
import os
import datetime
import sys

isGO = True
list = []


def sum_list(bool_list, n, now_sum):
    global isGO
    global list
    if isGO == False:
        return list
    if n >= len(sum_l):
        return
    if (now_sum + sum_l[n] == sum_num and sum_l[n] != 0):  # 如果原有值加上这个值正好为所求的数
        bool_list[n] = True  # 将这个数对应的数组值赋值为true
        list1 = []
        list2 = []
        for i, j in enumerate(bool_list):
            if j:
                # print(sum_l[i], end=' ')  # 输出所有对应值为true的值
                # print(i, end=' ')
                if sum_l[i] != 0:
                    list1.append(sum_l[i])
                    list2.append(i)
                    sum_l[i] = 0
        print('数值：', list1)
        print('序列：', list2)
        list = list1
        isGO = False
        # exit()#这是退出所有程序运行
        # print()
    bool_list[n] = True  # 如果这个数被选
    sum_list(bool_list, n + 1, now_sum + sum_l[n])  # 原来的sum和加上新的被选值
    bool_list[n] = False  # 如果没被选
    sum_list(bool_list, n + 1, now_sum)  # 原来的sum值不变
    return list


if __name__ == '__main__':
    print('请将data.csv文件置于同一文件夹下')
    path = './data.csv'
    sum_l1 = pd.read_csv(path)
    sum_input = input('Input the number of sum：')
    for i in range(len(sum_l1-24)):
        sum_l = sum_l1['data'][i:i+23].tolist()
        # sum_l = random.sample(range(15), 8)


        start = datetime.datetime.now()
        sum_num = float(sum_input)
        bool_list = [False for i in sum_l]
        sum_list(bool_list, 0, 0)

        # c={'data':sum_l}
        # new=pd.DataFrame(c)
        # new.to_csv('./data.csv') #保存索引列和name列
        print('done')
        # os.system('pause')
        end = datetime.datetime.now()
        print(end - start)

