class Queue:
    def _init_(self):
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

if _name_ == '_main_':
    q = Queue()
    q.enQueue(10)
    q.enQueue(11)
    q.enQueue(12)

    print(q.deQueue())
    print(q.deQueue())
    print(q.deQueue())
