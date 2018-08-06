# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 15:09:50 2018

"""

def hello(greeting,*args):
    if(len(args)==0):
        print('%s'%greeting)
    else:
        print('%s,%s'%(greeting,','.join(args)))#join()函数
#语法：  'sep'.join(seq),参数说明:sep：分隔符。可以为空,seq：要连接的元素序列、字符串、元组、字典
#上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串.返回值：返回一个以分隔符sep连接各个元素后生成的字符串

hello('Hi','Abby','Bob')
#tuple=['Abby','Bob']#wrong
#hello('Hi',*tuple)       
hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')

#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装 list 或 tuple，
再通过*args 传入：func(*(1, 2, 3))；
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')        
    