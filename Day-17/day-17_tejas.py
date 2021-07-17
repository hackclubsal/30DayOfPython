def createStack(queue):
    queue = []


def enqueue(stack, a):
    stack.append(a)


def dequeue(stack):
    stack.pop(0)


def prqueue(queue):
    print(queue)


q = []

enqueue(q, 9)
enqueue(q, 7)
dequeue(q)
enqueue(q, 8)
prqueue(q)
