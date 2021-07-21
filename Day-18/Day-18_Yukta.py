
class Node:
  
    
    def __init__(self, data):
        self.data = data  
        self.next = None  
                          
  

class LinkedList:
    
   
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

if __name__=='__main__':
    ll = LinkedList()    
    ll.head = Node(8)
    second = Node(10)

    ll.head.next = second

    ll.printList()