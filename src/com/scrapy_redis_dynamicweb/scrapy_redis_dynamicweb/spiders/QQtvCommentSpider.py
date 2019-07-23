#!/usr/bin/env python
#coding:utf-8

from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
import re
import json

import sys
sys.path.append("..")
from scrapy_redis_dynamicweb.items import ScrapyRedisDynamicwebItem

class CommentSpider(RedisSpider):
    name = "qqtvSpider"
    redis_key = "qqtvspider:start_urls"
    start_urls = ["http://v.qq.com/cover/q/qviv9yyjn83eyfu/v0016f0gu1h.html",]
    comment_url = "http://coral.qq.com/article/%s/comment?commentid=0&reqnum=20"
    sns_url = "http://sns.video.qq.com/fcgi-bin/video_comment_id?otype=json&callback=jQuery&op=3&vid="

    def parse(self, response):
        vid = re.search('vid:"(.*?)",', response.body, re.S).group(1)
        sns_url = self.sns_url + vid
        yield Request(sns_url, callback = "parse_id")

    def parse_id(self, response):
        cid = re.search('"comment_id":"(.*?)",', response.body, re.S).group(1)
        comment_url = self.comment_url % cid
        yield Request(comment_url, callback = "parse_comment")

    def parse_comment(self, response):
        jsDict = json.loads(response.body)
        jsData = jsDict["data"]
        comments = jsData["commentid"]
        for each in comments:
            item = ScrapyRedisDynamicwebItem()
            item["content"] = each["content"]
            item["name"] = each["userinfo"]["nick"]
            item["ctime"] = each["timeDifference"]
            yield item