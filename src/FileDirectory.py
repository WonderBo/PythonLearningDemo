#!/usr/bin/env python
#coding:utf-8

import os

def listDir(path):
    allFile = []
    subFile = os.listdir(path)      #列出当前路径下的目录或者文件，返回列表
    for fileName in subFile:
        fullFile = os.path.join(path, fileName)     #os提供方法连接路径与文件名形成完整路径名，作用同：字符串+“/”+字符串
        if os.path.isdir(fullFile):     #判断是否为目录或者文件，有isfile()方法
            listDir(fullFile)       #递归
        allFile.append(fullFile.decode('gbk').encode('utf-8'))      #对于中文的编码
        print fullFile.decode('gbk').encode('utf-8')
    return allFile
#递归方式获取文件目录
#递归方法的测试
#listDir("C:/Users/13160/Desktop")

#系统提供遍历目录的方法os.walk(path),返回3元元组（遍历路径名，目录列表，文件列表）
for path, dir, file in os.walk("C:/Users/13160/Desktop"):
    for f in file:
        print os.path.join(path, f).decode('gbk').encode('utf-8')
    for d in dir:
        print os.path.join(path, d).decode('gbk').encode('utf-8')