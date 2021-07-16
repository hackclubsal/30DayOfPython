def createStack(stack):
    stack = []


def addData(stack, a):
    stack.append(a)


def DelData(stack):
    stack.pop()


def prstack(stack):
    print(stack)


s = []

createStack(s)
addData(s, 3)
addData(s, 7)
addData(s, 4)
DelData(s)
addData(s, 8)

prstack(s)
