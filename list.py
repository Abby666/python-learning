# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:19:38 2018

"""
#the difference between list and tuple is list can modify 
#Python 内置的一种数据类型是列表：list。list 是一种有序的集合，可以随时添加和删除其中的元素。
#另一种有序列表叫元组：tuple。tuple 和 list 非常类似，但是 tuple 一旦初始化就不能修改
classmates=['Michael', 'Bob', 'Tracy']
print('classmates')
print(len(classmates))#output 3
print(classmates[-1])#the last name
classmates.append('Abby')
print('classmates=',classmates)#add Abby to the last
classmates.insert(1,'Lucy')
print('classmates=',classmates)#1 means insert the Bob on the second location
print(classmates.pop(0))#delect the first name
print('classmates=',classmates)
