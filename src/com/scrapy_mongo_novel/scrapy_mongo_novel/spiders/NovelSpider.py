#!/usr/bin/env python
#coding:utf-8

from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy_mongo_novel.items import ScrapyMongoNovelItem

class NovelSpider(CrawlSpider):
    name = "scrapy_mongo_novel"
    redis_key = "scrapy_mongo_novel:start_urls"
    start_urls = ["http://www.daomubiji.com/"]

    def parse(self, response):
        selector = Selector(response)
        for i in range(0, 11):
            # 为了防止后一个数据覆盖前一个数据（覆盖不全导致存储的数据有误），需要在每个循环里都实例化一个ScrapyMongoNovelItem
            item = ScrapyMongoNovelItem()

            novelURL = selector.xpath("//article/p/a/@href").extract()[i]
            novelName = selector.xpath("//article/div/h2/text()").extract()[i]
            novelIntro = selector.xpath("//article/div/p/text()").extract()[i]

            item["novelName"] = novelName
            item["novelIntro"] = novelIntro
            item["novelURL"] = novelURL
            yield item

            yield Request(novelURL, callback = self.parseNovel)

            #novelURL:即将访问的网页链接，callback:对即将访问的网页执行的操作，meta:传递给callback操作的参数字典，在callback操作通过item = response.meta['item']获取参数
            #yield Request(novelURL, callback='parseContent', meta={'item':item})

    def parseNovel(self, response):
        #先抓大
        selector = Selector(response)
        grabPart = selector.xpath("//article[@class = 'excerpt excerpt-c3']/a")

        #在抓小
        for eachChapter in grabPart:
            # 为了防止后一个数据覆盖前一个数据（覆盖不全导致存储的数据有误），需要在每个循环里都实例化一个ScrapyMongoNovelItem
            item = ScrapyMongoNovelItem()

            chapterURL = eachChapter.xpath("@href").extract()[0]
            infoString = eachChapter.xpath("text()").extract()[0]

            item["chapterURL"] = chapterURL
            # try可以用于检测错误，出现错误以后就会运行except里面的内容
            try:
                if len(infoString.split(" ")) == 2:
                    item["chapterName"] = infoString.split(" ")[0]
                    item["chapterNum"] = infoString.split(" ")[1]
                elif len(infoString.split(" ")) == 3 and (infoString != "沙海1 荒沙诡影 引子（一）" or infoString != "沙海1 荒沙诡影 引子（二）"):
                    item["chapterName"] = infoString.split(" ")[0]
                    item["chapterNum"] = infoString.split(" ")[1]
                    item["chapterTitle"] = infoString.split(" ")[2]
                elif len(infoString.split(" ")) == 4:
                    item["chapterName"] = infoString.split(" ")[0] + " " + infoString.split(" ")[1]
                    item["chapterNum"] = infoString.split(" ")[2]
                    item["chapterTitle"] = infoString.split(" ")[3]
                else:
                    item["chapterName"] = infoString.split(" ")[0] + " " + infoString.split(" ")[1]
                    item["chapterTitle"] = infoString.split(" ")[2]
                    item["chapterNum"] = infoString.split(" ")[2][-3:]
            except Exception, e:
                continue
            yield item