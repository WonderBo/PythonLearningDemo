#!/usr/bin/env python
#coding:utf-8

import  requests
import  re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class spider(object):
    def __init__(self):
        print u"开始爬取内容......"

    #去除字符串空格，换行符， table符
    def removeSpace(self, str):
        return str.replace(' ', '').replace('\n', "").replace('\t', '')

    #用来生产不同页数的链接
    def changePage(self, url, total_page):
        curr_page = int(re.search("pageNum=(\d+)", url, re.S).group(1))
        pageList = []
        for i in range(curr_page, total_page + 1):
            curr_url = re.sub("pageNum=\d+", "pageNum=%d" % i, url, re.S)
            pageList.append(curr_url)
        return pageList

    # 用来获取网页源代码
    def getHtmlSource(self, url):
        html = requests.get(url)
        return html.text

    #先抓大，在html页面用来抓取每个课程块的信息
    def parsePageFromWhole(self, source):
        lessonPart = re.findall('<div class="lesson-infor".*?</li>', source, re.S)
        return lessonPart

    #再抓小，用来从每个课程块中提取出我们需要的信息
    def parsePageFromPart(self, part):
        lessonInfo = {}
        lessonInfo["title"] = self.removeSpace(re.search('target="_blank".*?>(.*?)</a>', part, re.S).group(1))
        lessonInfo["content"] = self.removeSpace(re.search('<p style="height:.*?>(.*?)</p>', part, re.S).group(1))
        timeAndLevel = re.findall('<em>(.*?)</em>', part, re.S)
        lessonInfo["time"] = self.removeSpace(timeAndLevel[0])
        lessonInfo["level"] = self.removeSpace(timeAndLevel[1])
        lessonInfo["learnNum"] = self.removeSpace(re.search('<em class="learn-number".*?>(.*?)</em>', part, re.S).group(1))
        return lessonInfo

    #用来保存结果到course.txt文件中
    def saveInfo(self, lessonInfo):
        f = open("course.txt", "a")
        for each in lessonInfo:
            f.writelines("lessonTitle: " + each["title"] + "\n")
            f.writelines("lessonContent: " + each["content"] + "\n")
            f.writelines("lessonTime " + each["time"] + "\n")
            f.writelines("lessonLevel " + each["level"] + "\n")
            f.writelines("learnLearnNum: " + each["learnNum"] + "\n\n")
        f.close()


if __name__ == "__main__":
    spider = spider()
    url = "http://www.jikexueyuan.com/course/?pageNum=1"
    lessonList = []
    pageList = spider.changePage(url, 20)
    for pageUrl in pageList:
        print u"正在处理页面：" + pageUrl
        source = spider.getHtmlSource(pageUrl)
        lessonPart = spider.parsePageFromWhole(source)
        for lesson in lessonPart:
            lessonInfo = spider.parsePageFromPart(lesson)
            lessonList.append(lessonInfo)
    spider.saveInfo(lessonList)