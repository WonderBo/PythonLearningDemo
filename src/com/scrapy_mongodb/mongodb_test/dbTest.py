#!/usr/bin/env python
#coding:utf-8

import pymongo

#建立连接
connection = pymongo.MongoClient()
#确定对应数据库
db = connection.mongoTest
#确定对应文档
doc = db.person

kangkang = {"name": u"康康", "age": "22", "hobby": "reading"}
mike = {"name": "mike", "age": "23", "hobby": u"爬山", "skill": u"挖掘机"}
mary = {"name": "mary", "age": "24", "skill": "computer"}

# doc.insert(kangkang)
# doc.insert(mike)
# doc.insert(mary)
doc.remove({"name": u"康康"})

print u"操作数据库完成！"