# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 17:04:55 2018

"""

#任何可迭代对象都可以作用于 for 循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用 for 循环
#如list,tuple,dic
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

#默认情况下，dict 迭代的是 key。如果要迭代 value，可以用 for value in d.values()，
#如果要同时迭代 key 和 value，可以用 for k, v in d.items()
for key in d.values():
    print(key)
for key,v in d.items():
    print(key,v)

from collections import Iterable,Iterator
def g():
    yield 1#yield是一个关键词，类似return, 不同之处在于，yield返回的是一个生成器
    yield 2
    yield 3

#如何判断一个对象是可迭代对象呢？方法是通过 collections 模块的 Iterable 类型判断：
print('Iterable?[1,2,3]:',isinstance([1, 2, 3],Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator?g():', isinstance(g(), Iterator))
print('Iterator?123:', isinstance(123, Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):#iter() 函数用来生成迭代器
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))#next() 返回迭代器的下一个项目
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
#Python 内置的 enumerate 函数可以把一个 list 变成索引-元素对，这样就可以在 for 循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

