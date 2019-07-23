#coding:utf-8

import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 1
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, "%s.png" % x)
        x+=1
    
getImg(getHtml("http://sports.sohu.com/20170219/n481106288.shtml"))
