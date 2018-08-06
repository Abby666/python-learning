# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 16:13:38 2018

"""


def name_score(**kw):
    print('Name  Score')
    print('---------------------')
    for Name,Score in kw.items():
        print('%10s %d'%(Name,Score))
    print()
'''截取字符串输出,下面例子将只输出字符串的前3个字母      
>>> str="abcdefg"  
>>> print "%.3s" % str   
  abc   
按固定宽度输出，不足使用空格补全,下面例子输出宽度为10      
>>> str="abcdefg"  
>>> print "%10s" % str   
     abcdefg   
截取字符串，按照固定宽度输出      
>>> str="abcdefg"  
>>> print "%10.3s" % str   
         abc   
'''
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装 dict，再通过**kw 传入：func(**{'a': 1, 'b': 2})。
data={'Adam':99,'Lisa':88,'Bart':77}
name_score(**data)
name_score(Adam=99,Lisa=88)

#如果要限制关键字参数的名字，就可以用命名关键字参数
def personal_info(Name,Gender,*,City='Beijing',Age):
    print('Personal Info')
    print('--------------')
    print('Name:%s'% Name)
    print('Gender:%s'% Gender)
    print('City:%s'% City)
    print('Age:%d'% Age)
    print()
 #命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
personal_info('Bob', 'male',  Age=20)
#personal_info('Bob', 'male',  20)wrong ,loss the name of parameter 
personal_info('Lisa', 'female', City='Shanghai', Age=18)  

personal_info('Bob', Gender='male', Age=20)
personal_info(Name='Lisa', Gender='female', City='Shanghai', Age=18)
 






















