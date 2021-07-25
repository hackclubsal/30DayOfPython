# Day-21 Question for the day-21 is --->
# -> Question: Implement a Queue with the help of two stacks in Python 

# -> Input: 
# enqueue(10)
# enqueue(11)
# enqueue(12)
# -> Output: 
# 10
# 11
# 12


#day21
class queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def enqueue(self,x):
        self.stack1.append(x)

    def dequeue(self):
        if len(self.stack1)>0 and len(self.stack2) == 0:
            while len(self.stack1):
                temp = self.stack1.pop()
                self.stack2.append(temp)
            return self.stack2.pop()
 
        elif len(self.stack1) == 0 and len(self.stack2) == 0:
            print("Queue is Empty")
            return

        else:
            return self.stack2.pop()
 
if __name__ == '__main__':
    q = queue()
    q.enqueue(10)
    q.enqueue(11)
    q.enqueue(12)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    
  


        
