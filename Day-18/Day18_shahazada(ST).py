class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        newNode =Node(data)
        
        if(self.head):
            current = self.head
            while(current.next):
                current=curent.next
            current.next=newNode
        else:
            self.head=newNode
            
    def printLL(self):
        current=self.head
        while(current):
            print(current.data)
            current = current.next
            
            
if __name__ =='__main__':
    linkedlist =LinkedList()
    operations=1
    while(operations):
        operattions=int(input("If you want perform any operation enter 1 other wise 0:- "))
        if(not operattions):
            break;
        
        opcode=input('Enter insrt for insert operation ans prnt for print operation:- ').split()
        opcode = opcode[0].lower()
        
        if(opcode=='insrt'):
            data=input("Enter element for insert in linkedlist:- ")
            linkedlist.insert(data)
        elif(opcode=='prnt'):
            linkedlist.printLL()
        print()    
        
        
