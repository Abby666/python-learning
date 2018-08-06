# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:25:20 2018

"""

#set 和 dict 类似，也是一组 key 的集合，但不存储 value。要创建一个 set，需要提供一个 list 作为输入集合
classmates=set(['Michael', 'Bob', 'Tracy'])
print('classmates=',classmates)
classmates.add('Abby')
print('classmates=',classmates)
classmates.pop
print('classmates=',classmates)
classmates.remove('Bob')
print('classmates=',classmates)
#重复元素在 set 中自动被过滤：
s1=set([1,3,3,6])
print(s1)
#两个 set 可以做数学意义上的交集、并集等操作
s2=set([3,4,5])
print('s1&s2=',s1&s2)
print('s1|s2=',s1|s2)

#str 是不变对象，而 list 是可变对象。
a=['z','x','y']
a.sort()
print(a)

a='zxy'
a.replace('z','h')
print(a)#output is still 'zxy'