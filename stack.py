#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 12:29:58 2018

@author: yeoyoung
"""


#추상 자료형 (ADT) 구현
class BaseStack:
    # 데이터의 추가
    def push(self, data):
        pass
    # 데이터의 꺼내오기
    def pop(self):
        pass
    # 데이터 참조하기
    def top(self):
        pass
    
    #sub func
    # 비어있는지 확인
    def isEmpty(self):
        pass
    # 꽉 차있는지 확인
    def isFull(self):
        pass
    # 리스트 사이즈 출력
    def size(self):
        pass
    # 리스트 전체 출력
    def display(self):
        pass
    

        
class ArrayStack(BaseStack):
   def __init__(self, max_length=30):
     
     self.items = []
     self.high = 0  # high: 데이터를 ㅊ저장할 최신 위치
     self.max_length = max_length

   def push(self, data):
     if self.isFull():  # push할 수 있는지 확인
       raise Exception('스택이 꽉 찼습니다!')

     self.items.append(data)
     self.high += 1
     
     
   def pop(self):
       if self.isEmpty(): # pop할 수 있는지 확인
           raise Exception('스택이 비었습니다!')
 
       self.high -= 1
       data = self.items[self.high] #제일 먼저 들어온게 제일 위에
       del self.items[self.high]
  
       return data


   def top(self):
      if self.isEmpty():
          raise Exception('스택이 비었습니다!')

      return self.items[self.high - 1] # pop예정인 데이터를 참조한다. index 0부터 시작

   def isEmpty(self):
      return self.high == 0  # high이 0이면, 저장된 데이터가 하나도 없는 것 / push할 때마다 +1

   def isFull(self):
      # high==ㅇ max_length와 동일할 때 꽉참.
      return self.high == self.max_length
   
   def stackSize(self):
     if self.isEmpty():
         raise Exception('스택이 비었습니다!')
    
     return len(self.items)
    
   def display(self):
     if self.isEmpty():
       raise Exception('스택이 비었습니다!')
       
     for index in range(self.high):
         print(self.items[index])
         
stack=ArrayStack()
stack.push(3)
stack.push(4)
stack.display()
stack.stackSize()
stack.pop()
stack.pop()
stack.display()
stack.push(7)
stack.top()
stack.stackSize()
stack.pop()
stack.stackSize()
stack.isEmpty()
