#!/usr/bin/env python
#coding:utf-8

#open()或者file()创建或者打开文件
#r+:从文件起始位置开始覆盖写入
#w:删除原文件，重新写入
#a:从文件末尾位置开始写入
#b:针对二进制文件操作，比如图片
file_new = open("C:/Users/13160/Desktop/subpackage1.txt", "r+")

#read()或者write()进行读写，但是读写位置通常有一个‘指针’指示
#print file_new.read()
print file_new.readline()   #每次读取一行，读取完后返回空字符串
print file_new.readlines()  #读取所有行并返回列表
file_new.seek(0,0)  #操作指针位置
print file_new.next()   #每次读取一行，但是读取完毕后返回异常

#file_new.write("good")  

#close()关闭文件，不能对文件继续操作
file_new.close()