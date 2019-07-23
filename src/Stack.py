#!usr/bin/env python
#coding:utf-8

class Stack():
    #初始化
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1
    
    #入栈
    def push(self, content):
        if self.full():
            print "Stack is Full"
        else:
            self.stack.append(content)
            self.top += 1
    
    #出栈
    def pop(self):
        if self.empty():
            print "Stack is Empty"
        else:
            self.stack.pop()
            self.top -= 1
    
    #判断栈满
    def full(self):
        if self.top == self.size - 1:
            return True
        else:
            return False
    
    #判断栈空
    def empty(self):
        if self.top == -1:
            return True
        else:
            return False

#测试      
if __name__ == "__main__":
    print "初始化："
    stack = Stack(3)
    print stack.full(); print stack.empty()
    print "入栈："
    stack.push("wang")
    print stack.full(); print stack.empty()
    stack.push("bo"); stack.push("hello")
    print stack.full(); print stack.empty()
    print "出栈："
    stack.pop()
    print stack.full(); print stack.empty()
    stack.pop(); stack.pop()
    print stack.full(); print stack.empty()