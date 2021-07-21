# Day-18_Hackclubsal_30DayOfPython_Solution
# Program to Implement a LinkedList in Python

class Node:
  def __init__(self, info = None, link=None): 
    self.info = info
    self.link = link
class LinkedList:
  def __init__(self):  
    self.start = None
  def insert(self, info):
    newNode = Node(info)
    if(self.start):
      current = self.start
      while(current.link):
        current = current.link
      current.link = newNode
    else:
      self.start = newNode
  def printLL(self):
    current = self.start
    while(current):
      print(current.info)
      current = current.link


LL = LinkedList()
LL.insert(8)
LL.insert(10)
LL.printLL()
