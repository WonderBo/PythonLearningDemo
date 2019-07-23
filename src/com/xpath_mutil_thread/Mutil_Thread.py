#!/usr/bin/env python
#coding:utf-8

from multiprocessing.dummy import Pool as ThreadPool
import time
import requests

def getSource(url):
    html = requests.get(url)

urls = []

for i in range(0,20):
    newPage = "http://tieba.baidu.com/f?kw=java&ie=utf-8&pn=" + str(i*50)
    urls.append(newPage)

startTime = time.time()
for i in urls:
    print i
    getSource(i)
endTime = time.time()
print u"单线程耗时：" + str(endTime - startTime)

#线程数量
pool = ThreadPool(4)
startTime = time.time()
#多线程映射实现操作（同map-reduce思想中的map）
results = pool.map(getSource, urls)
pool.close()
pool.join()
endTime = time.time()
print u"并行耗时：" + str(endTime - startTime)