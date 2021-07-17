class Queue():
    def __init__(self):
        self.items=[]
   
         
    def is_empty(self):
       return self.items == []
    
    def enqueue(self,data):
        self.items.append(data)
    
    def dequeue(self):
        try:
            self.items.pop(0)
        except:
            print("queue has no element to pop")
    
    def display(self):
        print(self.items)
    

if __name__ == '__main__':
    queue=Queue()
    print('Following are the short hand key for operation:')
    print(['enq:for enque in queue','deq:for dequeue from queue','empt:for empty queue','prnt: for disply queue'])
    while(True):
        yn=int(input('If you want to perform any operation enter 1 other wise 0:- '))
        
        if(not yn):
            break;
        operation=input("Enter short hand for operationion you want to perform:- ").split()
        opr=operation[0].lower()
        if(opr=='enq'):
            ele=input("Enter elment you want to enqueue:- ")
            queue.enqueue(ele)
        
        elif(opr=='deq'):
            queue.dequeue()
        
        elif(opr=='empt'):
            queue.is_empty()
        elif(opr=='prnt'):
            queue.display()
        else:
            print('Apply a correct short hand: -')
        print()
        
    print("Your Final queue : ",queue.display())    
            
        
