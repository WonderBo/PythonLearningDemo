#!/usr/bin/env python
#coding:utf-8

import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy_doubanmovie.items import ScrapyDoubanmovieItem

class DoubanMovie(CrawlSpider):
    #此处的爬虫名应与main里面的运行爬虫名一致
    name = "scrapy_doubanmovie"
    redis_key = "scrapy_doubanmovie:start_urls"
    start_urls = ["http://movie.douban.com/top250"]

    url = "http://movie.douban.com/top250"

    def parse(self, response):
        #初始化item字典
        item = ScrapyDoubanmovieItem()

        #先抓大
        selector = Selector(response)
        movies = selector.xpath("//div[@class = 'info']")

        #再抓小
        for eachMovie in movies:
            #电影标题列表抓取
            title = eachMovie.xpath("div[@class = 'hd']/a/span/text()").extract()
            fullTitle = ""
            for eachTitle in title:
                fullTitle += eachTitle
            #电影信息列表抓取
            info = eachMovie.xpath("div[@class = 'bd']/p/text()").extract()
            #电影星级抓取
            star = eachMovie.xpath("div[@class = 'bd']/div[@class = 'star']/span[@class = 'rating_num']/text()").extract()[0]
            #电影引述列表抓取
            quote = eachMovie.xpath("div[@class = 'bd']/p[@class = 'quote']/span/text()").extract()

            #电影quote可能为空，因此需要先进行判断
            if quote:
                quote = quote[0]
            else:
                quote = ""

            #将抓取的各项内容封装入item字典
            item["title"] = fullTitle
            #"分隔符".join(列表) 表示用分隔符将列表连接成字符串
            item["info"] = ";".join(info)
            item["star"] = star
            item["quote"] = quote
            yield item

            #抓取‘下页’的链接列表
            nextLink = selector.xpath("//span[@class = 'next']/link/@href").extract()
            #最后一页没有下一页的链接，因此需要进行判断
            if nextLink:
                nextLink = nextLink[0]
                print nextLink
                yield Request(self.url + nextLink, callback = self.parse)