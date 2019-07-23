# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ScrapyMongoNovelItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #小说doc对应key
    novelName = Field()
    novelIntro = Field()
    novelURL = Field()

    #章节doc对应key
    chapterName = Field()
    chapterNum = Field()
    chapterURL = Field()
    chapterTitle = Field()
