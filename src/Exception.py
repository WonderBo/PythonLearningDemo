#!/usr/bin/env python
#coding:utf-8

fileInput = raw_input("请输入打开的文件路径: ")

#捕获异常
try:
    f = open(fileInput)
    print 'hello'
except IOError, msg:
    print "输入文件不存在"
except NameError, msg:
    print "内部变量调用错误"
finally:
    try:
        f.close
    except NameError, msg:
        pass

#抛出异常
if fileInput == "hello":
    raise NameError("错误----")
