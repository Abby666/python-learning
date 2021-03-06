# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 16:49:05 2018

"""

#对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python 提供了切片（Slice）操作符
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])#取前三个元素，从索引0开始到3,不包括3
print('L[:3] =', L[:3])#如果第一个索引是 0，还可以省略
print('L[1:3] =', L[1:3])#也可以从索引 1 开始，取出 2 个元素出来
print('L[-2:] =', L[-2:])#Python 支持 L[-1]取倒数第一个元素，那么它同样支持倒数切片
print('L[-2:] =', L[-2:-1])

R = list(range(100))
print('R[:10] =', R[:10])#前10个数
print('R[-10:] =', R[-10:])#后10个数
print('R[10:20] =', R[10:20])#前11到20个数
print('R[:10:2] =', R[:10:2])#前 10 个数，每两个取一个
print('R[::5] =', R[::5])#所有数，每 5 个取一个
print('R[:] =', R[:])#只写[:]就可以原样复制一个 list：


#tuple 也是一种 list，唯一区别是 tuple 不可变。因此，tuple 也可以用切片操作，只是操作的结果仍是 tuple
print( (0, 1, 2, 3, 4, 5)[:3])
