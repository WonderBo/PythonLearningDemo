#!/usr/bin/env python
#coding:utf-8

def add(x, y):
    return x+y

print __name__  #python内置变量，用于区分执行或者导入

#让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行
if __name__ == "__main__":
    print __name__, "Add.py被执行"
else:
    print __name__, "Add.py被导入"
