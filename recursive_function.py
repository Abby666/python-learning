# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 17:02:14 2018

"""

#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层
#栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
#解决递归调用栈溢出的方法是通过尾递归优化，把循环看成是一种特殊的尾递归函数也是可以的
#尾递归是指，在函数返回的时候，调用自身本身，并且，return 语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))    


# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> c
# A --> C
def move(n, a, b, c):
    if n==1:
        print('move',a,'-->',c)
    else:
        move(n-1,a,c,b)
        print('move',a,'-->',c)
        move(n-1,b,a,c)
print(move(3,'A','B','C'))










