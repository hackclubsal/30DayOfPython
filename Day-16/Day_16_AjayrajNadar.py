def create(stack):
    stack = []
def add(stack, a):
    stack.append(a)
def Del(stack):
    stack.pop()
def pr(stack):
    print(stack)
s = []
createStack(s)
addData(s, 3)
addData(s, 7)
addData(s, 4)
DelData(s)
addData(s, 8)

prstack(s)
