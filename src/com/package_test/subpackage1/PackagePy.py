#!/usr/bin/env python
#coding:utf-8

#同级目录或子目录模块导入
import PrintPy
PrintPy.printTest()

#上级目录模块导入
import sys
sys.path.append("..")
#更普遍的办法是在python 安装目录的site-package文件夹中新建xxx.pth（我的是myMod.pth），内容是需要导入的package所在的文件夹绝对路径，然后可以直接导入
#需要注意的是具有层次关系的包的包名不能相同，即package1.package1是不合法的

#import方式导入（导入相应包，调用方法时需要相应路径）
import subpackage2.Add
print subpackage2.Add.add(1, 4)

#import as方式导入（导入包并取别名）
import subpackage2.Add as add
print add.add(1, 4)

#from import方式导入（导入包的具体方法）
from subpackage2.Add import *
print add(1, 4)