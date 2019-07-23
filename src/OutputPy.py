#!/usr/bin/env python
#coding:utf-8

#python里面的字符，如果开头处有个r,说明字符串r"XXX"中的XXX是普通字符
#与普通字符相比，其他相对特殊的字符，其中可能包含转义字符，即那些，反斜杠加上对应字母，表示对应的特殊含义的，比如最常见的”\n"表示换行，"\t"表示Tab等，如果是以r开头，那么说明后面的字符，都是普通的字符
#以r开头的字符，常用于正则表达式，对应着re模块
print r"/n/n/n/n/t/t/t"

#Unicode是书写国际文本的标准方法。如果你想要用非英语写文本,那么你需要有一个支持Unicode的编辑器
#Python允许你处理Unicode文本——你只需要在字符串前加上前缀u或U
print u"This is a Unicode string"