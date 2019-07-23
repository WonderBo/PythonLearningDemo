#!/usr/bin/env python
#coding:utf-8

import requests
html = requests.get('http://www.jikexueyuan.com/course.txt/821_2.html?ss=1')
print html.text