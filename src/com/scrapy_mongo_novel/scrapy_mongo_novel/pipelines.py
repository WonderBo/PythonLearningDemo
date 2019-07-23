# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class ScrapyMongoNovelPipeline(object):

    def __init__(self):
        #读取settings里的参数
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        novelDocName = settings['MONGODB_NOVELDOCNAME']
        chapterDocName = settings['MONGODB_CHAPTERDOCNAME']

        #与mongodb建立连接，并逐步获取相应数据库与文档
        client = pymongo.MongoClient(host = host, port = port)
        db = client[dbName]
        self.novelDoc = db[novelDocName]
        self.chapterDoc = db[chapterDocName]

    def process_item(self, item, spider):
        spiderDict = dict(item)
        #此处item与doc的关系为一对多
        #将爬取的数据根据类型加入不同的doc时需要进行判断，否则该数据会插入到所有doc中，无值时会设置为null
        #pipelines中根据字典键值读取数据只能使用dic.get(键值,[默认])，不能使用dic[键值]形式
        if spiderDict.get("novelName"):
            novelDict = {"NovelName" : spiderDict.get("novelName", u"暂无"), "NovelIntro" : spiderDict.get("novelIntro", u"暂无"), "NovelURL" : spiderDict.get("novelURL", u"暂无")}
            self.novelDoc.insert(novelDict)
        else:
            chapterDict = {"ChapterName" : spiderDict.get("chapterName", u"暂无"), "ChapterNum" : spiderDict.get("chapterNum", u"暂无"), "ChapterURL" : spiderDict.get("chapterURL", u"暂无"), "ChapterTitle" : spiderDict.get("chapterTitle", u"暂无")}
            self.chapterDoc.insert(chapterDict)
        return item
