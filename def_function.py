# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:52:32 2018

"""

def my_max(x,y):
    if x>y:
        return x
    else:
        return y
z=my_max(2,4)
print(z)
#       print(my_max(2,4))#wrong

#如果想定义一个什么事也不做的空函数，可以用 pass 语句
#pass 可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个 pass，让代码能运行起来。
def nop():
    pass

#参数检查
    #数据类型检查可以用内置函数 isinstance()实现：
def my_max(x,y):
    if not isinstance(x,(int,float)):#isinstance() 函数来判断一个对象是否是一个已知的类型
        raise TypeError('bad operand type')
    if not isinstance(y,(int,float)):#isinstance() 函数来判断一个对象是否是一个已知的类型
        raise TypeError('bad operand type')
    if x>y:
        return x
    else:
        return y
#    print(my_max(2,4)) 
print(my_max(2,4))      

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print( my_abs(-2))
   
#函数可以返回多个值
        #从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
import math#import math 语句表示导入 math 包，并允许后续代码引用 math 包里的 sin、cos 等函数。
def move(x,y,step,angle=0):
    nx=x+step*math.cos(x)
    ny=y-step*math.sin(y)
    return nx,ny
x, y = move(100, 100, 60, math.pi / 6)
print(x,y)