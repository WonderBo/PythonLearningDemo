#!/usr/bin/env python
#coding:utf-8

import sys, time
for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            #格式化输出
            print "%d*%d=%d" % (i, j, i*j),

            #python2:
            #print i, '*', j,'=', i*j, "\t",

            #python3:
            #print(i, '*', j,'=', i*j, "\t", end='')

            #标准输出（默认为sys.stdout = __console__（控制台），实际上可以给其赋任何有具有write方法的对象即可）
            # sys.stdout.write(str(i)+"*"+str(j)+"="+str(i*j)+"\t")
            # sys.stdout.flush()
            if i==j:
                print('\n')