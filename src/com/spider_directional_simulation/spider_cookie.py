#!/usr/bin/env python
#coding:utf-8

import requests
from lxml import etree

cookie = {"Cookie" : "_T_WM=73d0d7437a4cdc3654bf09d24212b49e; SUB=_2A250GSU5DeRhGeRH4lEZ8yjKzj-IHXVX4ktxrDV6PUJbkdAKLVb1kW0pDuEsfQWOJkiGZDJA7jGbwdFN1w..; SUHB=0laFw_96cCj7bH; SCF=ArX06gg9WDUancNP7Ny1TbGiAfyi-_lkk5BfVPMvpBYHOddQws1IttpJhQHdxmQp1vq7MWZGxjoEg_qo3vf9gpU.; SSOLoginState=1495094637"}
url = "https://weibo.cn/xuezhiqian"
#初始界面html
# html = requests.get(url).content
# print html

#使用cookie模拟登录后界面
html = requests.get(url, cookies = cookie).content
# print html

#text属性，用来表示纯文本内容，而非文本内容要使用content（比如图片，pdf）
#r.text返回的是Unicode型的数据，而使用r.content返回的是bytes型的数据,在使用r.content的时候，他已经进行将源代码转化成比特数组，然后再将比特数组转化成一个比特对象的转换
# html = requests.get(url, cookies = cookie).text
# html = bytes(bytearray(html, encoding = "UTF-8"))
# print html

#使用xpath获取关键消息
selector = etree.HTML(html)
content = selector.xpath("//span[@class='ctt']")
for each in content:
    text = each.xpath("string(.)")
    print text

