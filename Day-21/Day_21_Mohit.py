# program to implement Queue using two stacks

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self, x):

        while len(self.s1) != 0:
            self.s2.append(self.s1[-1])
            self.s1.pop()

        self.s1.append(x)

        while len(self.s2) != 0:
            self.s1.append(self.s2[-1])
            self.s2.pop()

    def deQueue(self):

        if len(self.s1) == 0:
            print("Q is Empty")

        x = self.s1[-1]
        self.s1.pop()
        return x


if __name__ == '__main__':
    q = Queue()
    n = int(input("Enter the Elements Range : "))
    for i in range(0, n):
        ele = int(input("Enqueue : "))
        q.enQueue(ele)

    for a in range(0, n):
        print(q.deQueue())
