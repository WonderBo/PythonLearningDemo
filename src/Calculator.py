#!/usr/bin/env python
#coding:utf-8

from __future__ import division

#利用字典代替switch语法实现分支运算
dic = {"+":lambda x,y:x+y , "-":lambda x,y:x-y , "*":lambda x,y:x*y , "/":lambda x,y:x/y}   #lambda函数返回的是函数对象

def cal(x,c,y):
    print dic.get(c)(x,y)   #dic.get(c)取出字典内的函数对象，并赋予x,y参数值   eg.fun(x,y)函数中fun为函数对象
    
cal(3,"/",2)



#lambda函数用例
fun = lambda x,y:x+y    #fun就为一函数对象
print fun
print cal
print fun(1,2)