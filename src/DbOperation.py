#!/usr/bin/env python
#coding:utf-8

import MySQLdb

#Connect() 方法用于创建数据库的连接，里面可以指定参数：用户名，密码，主机等信息
conn = MySQLdb.connect(
                       host="127.0.0.1", 
                       port=3306, 
                       user="root", 
                       passwd="justdoit111757", 
                       db="pytest"
                       )
#通过获取到的数据库连接conn下的cursor()方法来创建游标
cur = conn.cursor();
#插入一条数据
def insertOne():
    sqli = "insert into user values(%s, %s)"
    cur.execute(sqli, ("mary", "male"))     #插入一条数据以元组形式插入
    cur.close()
    conn.commit()
    conn.close()

#插入多条数据
def insertMany():
    sqli = "insert into user values(%s, %s)"
    cur.executemany(sqli, [("mary", "male"),("mike", "female")])    #插入多条数据以列表形式插入
    cur.close()
    conn.commit()
    conn.close()
    
#查询一条数据
def searchOne():
    sqls = "select * from user"
    cur.execute(sqls);    #返回表中数据条数
    print cur.fetchone()     #每执行一次，游标会从表中的第一条数据移动到下一条数据的位置，以元组形式返回行数据
    print cur.fetchone()
    cur.scroll(0, "absolute")   #将游标定位到表中的第一条数据（第一参数代表移动距离，第二参数代表开始移动位置）
    print cur.fetchone()
    cur.close()
    conn.close()
    
#查询多条数据
def searchMany():
    sqls = "select * from user"
    num = cur.execute(sqls);    #返回表中数据条数
    print num
    list = cur.fetchmany(num)   #以列表形式(元组为单位)返回表中所有数据
    for l in list:
        print l
    cur.close()
    conn.close()
    
#修改数据
def update():
    sqlu = "update user set gender = 'female' where name = 'mary'"
    cur.execute(sqlu)
    cur.close()
    conn.commit()
    conn.close()

#删除数据
def delete():
    sqld = "delete from user where name = 'mary'"
    cur.execute(sqld)
    cur.close()
    conn.commit()
    conn.close()

#测试
#insertOne()
#insertMany()
#searchOne()
#searchMany()
#update()
#delete()