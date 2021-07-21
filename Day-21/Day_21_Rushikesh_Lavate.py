"""Implement a Queue with the help of two stacks in Python"""


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

class Queue:
    def __init__(self):
        self.stack_1=[]
        self.stack_2=[]

    def enqueue(self,ele):
        self.stack_1.append(ele)
        print(self.stack_1)


    def dequeue(self):
        if len(self.stack_2)==0 and len(self.stack_1)==0:
            print("Queue is empty")
            return
        elif len(self.stack_2)==0 and len(self.stack_1)>0:
            while(self.stack_1):
                item=self.stack_1.pop()
                self.stack_2.append(item)
            result = self.stack_2.pop()
            print(result,' popped')
            return result


        else:
            result = self.stack_2.pop()
            print(result, ' popped')
            return result
if __name__ == '__main__':
    queue = Queue()

    while True:
        choice=int(input("Choose :  1) enqueue 2) dequeue "))
        if choice==1:
            ele = int(input("Enter element : "))
            queue.enqueue(ele)
        elif choice==2:
            queue.dequeue()
        else:
            print("Please enter the correct choice :  ")
