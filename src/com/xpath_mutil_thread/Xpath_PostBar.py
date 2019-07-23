#!/usr/bin/env python
#coding:utf-8

from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def writeFile(contentDir, f):
    f.writelines(u"回帖时间：" + str(contentDir["time"]) + "\n")
    f.writelines(u"回帖内容：" + unicode(contentDir["content"]) + "\n")
    f.writelines(u"回帖人：" + contentDir["author"] + "\n\n")

def spider(link):
    html = requests.get(link)
    selector = etree.HTML(html.text)
    #先抓大
    content_field = selector.xpath("//div[@class='l_post j_l_post l_post_bright  ']")
    f = open("content.txt", "a")
    item = {}
    for each in content_field:
        #再抓小
        #json格式数据转化为字典形式进行解析
        reply_info = json.loads(each.xpath("@data-field")[0].replace("&quot", ""))
        reply_author = reply_info["author"]["user_name"]
        reply_content = each.xpath("div[@class='d_post_content_main']/div/cc/div[@class='d_post_content j_d_post_content  clearfix']/text()")[0]
        reply_time = reply_info["content"]["date"]
        #输出抓取的信息
        print reply_content
        print reply_time
        print reply_author
        #抓取的信息封装到字典中
        item["author"] = reply_author
        item["content"] = reply_content
        item["time"] = reply_time
        #将字典写入到文件里
        writeFile(item, f)
    f.close()

if __name__ == "__main__":
    pool = ThreadPool(4)
    pageList = []
    for i in range(1,3):
        url = "http://tieba.baidu.com/p/5104640998?pn=" + str(i)
        pageList.append(url)
    results = pool.map(spider, pageList)
    pool.close()
    pool.join()
