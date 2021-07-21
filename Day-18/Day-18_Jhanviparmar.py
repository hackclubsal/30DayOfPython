#day18
class Node:
    def __init__(self, data = None, next = None): 
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

  def printll(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

ll = LinkedList()
ll.insert(3)
ll.insert(5)
ll.insert(15)
ll.printll()
