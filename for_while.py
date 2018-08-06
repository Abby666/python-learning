# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 15:04:24 2018

"""

#for x in ...循环就是把每个元素代入变量 x，然后执行后续
#list()函数可以转换为 list。比如 range(5)生成的序列是从 0 开始小于 5 的整数
#程序陷入“死循环”，可以用 Ctrl+C退出程序，或者强制结束 Python 进程
classmates=['Michael', 'Bob', 'Tracy']
for x in classmates:
    print(x)
for y in range(5):
    print(y)

z=1
while z<3:
    z=z+1
print(z)
print(10)

sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print(sum)