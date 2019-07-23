#!/usr/bin/env python
#coding:utf-8

import requests
import re
#下面三行是编码转换的功能，大家现在不用关心。
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#header是我们自己构造的一个字典，里面保存了user-agent
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
#部分网站对爬虫程序进行过滤，因此爬虫需包含浏览器头部伪装成浏览器
# html = requests.get('http://jp.tingroom.com/yuedu/yd300p/')
html = requests.get('http://jp.tingroom.com/yuedu/yd300p/',headers = header)

html.encoding = 'utf-8' #这一行是将编码转为utf-8否则中文会显示乱码。
# print html.text
# title = re.findall('color:#666666;">(.*?)</span>',html.text,re.S)
# for each in title:
#     print each
#
chinese = re.findall('color: #039;">(.*?)</a>',html.text,re.S)
for each in chinese:
    print each