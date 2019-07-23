#!/usr/bin/env python
#coding:utf-8

class Programer(object):
    hobby = "play computer"
    #magic method（内建方法）
    #创建类的对象
    def __new__(cls, *args, **kwargs):
        print args
        return super(Programer, cls).__new__(cls, *args, **kwargs)
        
    #实例化类的对象
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception("age must be int")
    #类与运算符
    def __eq__(self, other):
        if isinstance(other, Programer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception("The type of object must be Programer")
        
    def __add__(self, other):
        if isinstance(other, Programer):
            return self.age + other.age
        else:
            raise Exception("The type of object must be Programer")
    #类的展现
    def __str__(self):
        return "%s is %s years old" % (self.name, self.age)    
    
    def __dir__(self):
        return self.__dict__.keys()
    
    #类的属性控制
    def __getattribute__(self, name):
#        return getattr(self, name)        错误示例，导致无限递归
#        return self.__dict__[name]        错误示例，导致无限递归
        return super(Programer, self).__getattribute__(name)
    
    def __setattr__(self, name, value):
#        setattr(self, name, value)        错误示例，导致无限递归
        self.__dict__[name] = value         
    
    #类方法，直接用类去调用
    @classmethod
    def getHobby(cls):
        return cls.hobby
    
    #以属性的方式调用该方法
    @property
    def getAge(self):
        return self.age
    
    def self_intro(self):
        print "My name is %s \n I am %s years old" % (self.name, self.getAge)

#继承        
class BackProgramer(Programer):
    #__atr表示“私有”属性，只允许在类中直接调用它，在类外不能直接调用，但是可以通过_Class__atr形式在类外调用（访问控制），实际上只是修改属性名称，并没访问控制
    def __init__(self, name, age, language):
        self.__language = language
        super(BackProgramer, self).__init__(name, age)
    
    #继承方法重写
    def self_intro(self):
        print "My name is %s \tI am %s years old \tMy language is %s" % (self.name, self.getAge, self.__language)

if __name__ == "__main__":
    p_1 = Programer("jack", 23)
    p_2 = Programer("mary", 24)
    
    #dir()：所做的不是查找一个对象的__dict__属性（这个属性有时甚至都不存在），它使用的是对象的继承关系来反馈一个对象的完整的有效属性
    #__dict__：一个实例的__dict__属性仅仅是那个实例的局部属性集合，不包含该实例所有有效属性
    print dir(Programer)
    print dir(p_1)
    print Programer.__dict__
    print p_1.__dict__
    
    #多态条件：（1）继承 （2）方法重写  多态可以看作是“披着羊皮的狼”
    p_3 = BackProgramer("kang", 25, "java")
    if isinstance(p_3, Programer):
        p_3.self_intro()
    print p_3._BackProgramer__language
    
    #类与运算符测试
    print p_1 == p_2
    print p_1 + p_2
    
    #类的展现测试
    print p_1
    print dir(p_1)
    
    #类的属性控制测试
    print p_2.name
