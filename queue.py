#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 12:29:58 2018

@author: yeoyoung
"""

class BaseQueue:
    # 데이터의 추가
    def enqueue(self, data):
        pass
    # 데이터의 꺼내오기
    def dequeue(self):
        pass
    #sub func
    # 데이터 참조하기
    def front(self):
        pass
    # 비어있는지 확인
    def isEmpty(self):
        pass
    # 꽉 차있는지 확인
    def isFull(self):
        pass
    # 리스트 전체 출력
    def display(self):
        pass
    
class ArrayQueue(BaseQueue):

     
   def __init__(self, max_length=30):

       self.items = []
       self.size = self.first = self.last = 0 #순서가 있기 때문에. / size 큐 크기
       self.max_length = max_length
       
   def enqueue(self, data):
       if self.isFull():  # enqueue할 수 있는지 확인
           raise Exception('큐가 꽉 찼습니다!')
           
       self.items.append(data)    
       self.items[self.last] = data
       self.last += 1
       self.size += 1


   def dequeue(self):
       if self.isEmpty(): # dequeue 수 있는지 확인
           raise Exception('큐가 비었습니다!')
 
       data = self.items[self.first]
       self.items[self.first]=None
       
       self.first += 1
       self.size -= 1
       
       return data

   def front(self):
       if self.isEmpty():
           raise Exception('큐가 비었습니다!')
       return self.items[self.first]
       
   def isEmpty(self):
       return self.size == 0  
   
   def isFull(self):
     
       return self.size == self.max_length
   
   def queueSize(self):
       if self.isEmpty():
          raise Exception('큐가 비었습니다!')

       return self.size
    
   def display(self):
       if self.isEmpty():
          raise Exception('큐가 비었습니다!')
       
       for index in range(self.size):
          print(self.items[index])
          
queue=ArrayQueue()
queue.enqueue(3)
queue.enqueue(4)
queue.display()
queue.queueSize()
queue.dequeue()
queue.queueSize()
queue.dequeue()
queue.display()
queue.enqueue(7)
queue.front()
queue.queueSize()
queue.dequeue()
queue.display()
queue.isEmpty()

