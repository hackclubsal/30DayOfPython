class MyQueue(object):

    def __init__(self):
        self.sfront = []
        self.srever = []

    def push(self, x):

        self.sfront.append(x)

    def pop(self):


        if len(self.sfront) == 0 and len(self.srever) == 0:
            print("Q is Empty")
            return


        elif len(self.srever) == 0 and len(self.sfront) > 0:
            while len(self.sfront):
                temp = self.sfront.pop()
                self.srever.append(temp)
            return self.srever.pop()

        else:
            return self.srever.pop()

if __name__ == '__main__':
    q = MyQueue()
    q.push(10)
    q.push(11)
    q.push(12)

    print(q.pop())
    print(q.pop())
    print(q.pop())