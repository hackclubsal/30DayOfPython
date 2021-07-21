'''Question: Implement a Queue with the help of two stacks in Python 

-> Input: 
enqueue(10)
enqueue(11)
enqueue(12)

-> Output: 
10
11
12
'''
'''
#Python3 program to Implement Queue using two  stacks with costly enQueue() 
class Queue :
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def enQueue(self,x):
        
        # Move all elements from s1 to s2
        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
            
        #push item into self.s1
        self.s1.append(x)
        
        
        #push everything backto s1
        while len(self.s2) !=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
        
    # Dequeue an item stack is empty
    def deQueue(self):
        
        if len(self.s1) ==0:
            print("Q is Empty")
            
        #Return top of self.s1
        x = self.s1[-1] 
        self.s1.pop()
        return x
'''
'''
class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    
    def enQueue(self,x):
        self.s1.append(x)
    
    def deQueue(self):
        if len(self.s1)==0 and len(self.s2)==0:
            pritn("Q is empty")
            return 
        elif(len(self.s2)==0 and len(self.s1)>0):
            while len(self.s1):
                temp=self.s1.pop()
                self.s2.append(temp)
            return self.s2.pop()
        else:
            return self.s2.pop()
            
    


#driver unicode
if __name__ == '__main__':
    q=Queue()
    q.enQueue(1)
    q.enQueue(2)
    q.enQueue(3)
    
    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
'''
class Queue:
    def __init__(self):
        self.st1=[]
        self.st2=[]
    
    def enQueue(self,ele):
        self.st1.append(ele)
        print("{} is inserted into Queue".format(ele))
        
        
    def deQueue(self):
        if len(self.st2)==0 and len(self.st1)==0:
            print("Queue is empty")
            return 
        elif len(self.st2)==0 and len(self.st1)>0:
            while(self.st1):
                item=self.st1.pop()
                self.st2.append(item)
            return self.st2.pop()
        else:
            return self.st2.pop()
            
if __name__ == '__main__':
    queue = Queue()
    
    while(1):
        yn=int(input("If you don't want to perform any operation enter 0 other wise enter any number:- "))
        if(not yn):
            break;
        choice=input("Enter 'enq' for insert into Queue and 'deq' for pop from Queue:- ").split()
        choice=choice[0].lower()
        
        if choice=='enq':
            ele=int(input("Enter element to be insert into Queue:- "))
            queue.enQueue(ele)
            print()
        elif choice=='deq':
            print("{} is poped from Queue".format(queue.deQueue()))
            print()
        else:
            print("OOps! Wrong Choice ")
            print()
            
            
            
