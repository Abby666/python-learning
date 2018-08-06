# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:23:09 2018

"""

#Python 内置了字典：dict 的支持，dict 全称 dictionary，
#dict特点：1. 查找和插入的速度极快，不会随着 key 的增加而增加；2. 需要占用大量的内存
classmates = {'Michael': 30,'Bob': 40, 'Tracy': 50 }
print(classmates['Michael'])#查找对应分数

#dict第二种实现方式,把数据放入 dict 的方法，除了初始化时指定外，还可以通过 key 放入
classmates['Michael']=30
print(classmates['Michael'])
print('classmates[\'Michael\'] =', classmates['Michael'])
#要避免 key 不存在的错误，有两种办法，一是通过 in 判断 key 是否存在：
#通过 key 计算位置的算法称为哈希算法（Hash）。
'Michael' in classmates
#通过 dict 提供的 get 方法，如果 key 不存在，可以返回 None，或者自己指定的 value：
classmates.get('Abby',-1)
classmates.get('Michael')
classmates.get('Michael',-1)
#要删除一个 key，用 pop(key)方法，对应的 value 也会从 dict 中删除：
classmates = {'Michael': 30,'Bob': 40, 'Tracy': 50 }
classmates.pop('Michael')
print('classmates=',classmates)
classmates.pop('Abby',-1)



