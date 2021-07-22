# Day-21_Hackclubsal_30DayOfPython_Solution
#Program to  Implement a Queue with the help of two stacks in Python 

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enQueue(self, x):

        while len(self.stack1) != 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()
        self.stack1.append(x)

        while len(self.stack2) != 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

    def deQueue(self):

        if len(self.stack1) == 0:
            print("Q is Empty")
        x = self.stack1[-1]
        self.stack1.pop()
        return x

if __name__ == '__main__':
    q = Queue()
    q.enQueue(10)
    q.enQueue(11)
    q.enQueue(12)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
