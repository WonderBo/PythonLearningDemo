#!/usr/bin/env python
#coding:utf-8

#传入函数的参数可以为整型，字符串，元组，列表，字典
def fun(x):
    print x
fun(x="jack")    
fun(("jack",23,"male"))
fun(["jack",23,"male"])
fun(range(10))      #range函数返回列表
fun({"name":"jack","age":23,"gender":"male"})


#传入函数的参数为元组或者字典，可以利用*或者**取元组或字典所有值为多个形参赋值    注意：所有值
print "\n"
def fun_1(name,age):
    print name
    print age

tup = ("jack",23)
tup_2 = ("jack",23,"male")  #会报错
dic = {"name":"jack","age":23}
dic_2 = {"name":"jack","age":23,"gender":"male"}  #会报错

fun_1(*tup)
fun_1(**dic)    #传入字典时，形参名称必须与字典中键的名称与数量一一对应


#当传入函数的参数的数量多于形参数量时，可以用元组和字典来收纳多于的传入参数（元组收纳多余的值，字典收纳多余的键值对）
print "\n"
def fun_2(x,*tup,**dic):
    print x
    print tup
    print dic
    
fun_2("jack")
fun_2("jack",23,"male")
fun_2("jack",age=23)
fun_2(x="jack",age=23)
fun_2("jack","male",age=23) 
#fun_2("jack",age=23,"male")     #会报错，键值对后面的所有参数必须也以键值对的形式给出（即包含键值对形式的参数都应该从右开始依次给出，这点在形参赋值和缺省参数位置是相同的）
#fun_2("jack","male",x="kang")  #会报错，形参x传入了多个值，只是传入形式不同而已