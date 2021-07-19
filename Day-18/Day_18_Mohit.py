class Node:

    def __init__(self, data=None, next=None):
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
            print(current.data)
            current = current.next


i = int(input("Enter the element : "))
j = int(input("Enter the element : "))

LL = LinkedList()
LL.insert(i)
LL.insert(j)
LL.printLL()
