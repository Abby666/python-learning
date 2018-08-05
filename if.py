# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:41:24 2018

"""

# 注意:
# input()返回的是字符串
# 必须通过int()将字符串转换为整数
# 才能用于数值比较:
s=input('input your age:')
age=int(s)
if age>18:
    print('adult')
elif age>6:
    print('teenager')
else:
    print('baby')