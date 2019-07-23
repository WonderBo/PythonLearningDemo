#!/usr/bin/env python
#coding:utf-8

import requests
import re

url = 'https://www.crowdfunder.com/'
url_new = 'https://www.crowdfunder.com/browse/deals&template=false'


# html = requests.get(url)
# html.encoding = 'utf-8'
# print html.text


#注意这里的page后面跟的数字需要放到引号里面。
data = {
    'entities_only':'true',
    'page':'2'
}
#Post提交数据，并接收返回的结果
html_post = requests.post(url_new,data=data)
title = re.findall('"card-title">(.*?)</div>',html_post.text,re.S)
for each in title:
    print each