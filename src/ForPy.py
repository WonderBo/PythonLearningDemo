#!/usr/bin/env python
#coding:utf-8

import time

str = "jack"    #字符串String
tup = ("jack" , 23 , "male")   #元组Tuple
list = ["jack" , 23 , "male"]  #列表List
dic = {"name":"jack" , "age":23 , "gender":"male"}  #字典Dictory

for x in str:
    print x

for y in range(0 , len(tup) , 1):
    print "index:" , y
    print "context:" , tup[y]
    
for d in dic:
    print d
    print dic[d]

for k,v in dic.items():
    print "key:",k
    print "value:",v 
else:                       #for，while循环正常结束后执行,break或者其它中断不为正常结束
    print "ending"
    
print "\n"

for t in range(1,11):
    print t
    if t == 2:
        pass    #代码桩   用于占位，不产生任何效果
    elif t == 3:
        continue    #跳到下次循环，不执行此次循环后面的代码
    elif t == 5:
        exit()  #结束代码执行
    elif t == 6:
        break   #跳出此个循环，包括else部分
    print "-" * 20
    time.sleep(1)
else:
    print "结束"