#! usr/bin/env python
# coding:utf-8

class Queue():
    #初始化
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.head = -1
        self.tail = -1
    
    #入队列
    def enQueue(self, content):
        if self.full():
            print "Queue is Full"
        else:
            self.queue.append(content)
            self.tail += 1
    
    #出队列
    def deQueue(self):
        if self.empty():
            print "Queue is Empty"
        else:
            self.queue.pop(0)
            self.tail -= 1      #不为循环队列
    
    #判断队列空
    def empty(self):
        if self.head == self.tail:
            return True
        else:
            return False
    
    #判断队列满 
    def full(self):
        if self.tail - self.head == self.size:
            return True
        else:
            return False
    
#测试
if __name__ == "__main__":
    print "初始化："
    queue = Queue(3);
    print queue.full(); print queue.empty()
    print "入队："
    queue.enQueue("wang")
    print queue.full(); print queue.empty()
    queue.enQueue("bo"); queue.enQueue("hello");
    print queue.full(); print queue.empty()
    print "出队："
    queue.deQueue()
    print queue.full(); print queue.empty()
    queue.deQueue(); queue.deQueue()
    print queue.full(); print queue.empty()