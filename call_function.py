# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:35:42 2018

"""

print(abs(-2))
print(max(2,4))
print(int(12.34))
#print(int('12.34'))#wrong
print(int('12'))
print(str(12.34))
print(bool(12.34))

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a=abs
print(a(-1))
