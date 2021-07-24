# Day-18 Question for the day-18 is --->

# -> Question: Implement a Singly LinkedList in Python.

# -> Input: 
# Add(8)
# Add(10)
# Print ()

# -> Output: 
# 8, 10

# Note: just perform addition and printing it's elements operations.

# Hint: 
# LinkedIn list are collections of Nodes which are linked with each other by a pointer.

# Two main components in LinkedList.

# 1:Node
# 2:next pointer (pointing to the next node)
# 3: head (first node the LinkedList)

# Create two python classes one for LinkedList and another for Node.

# In LinkedList class define header and in Node class define next pointer.


class Node:

  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):  
    self.head = None

  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

  def printLL(self):
    current = self.head
    while(current):
      print(current.data, sep=",",end=" ")
      current = current.next


LL = LinkedList()
LL.insert(8)
LL.insert(10)
LL.printLL()
