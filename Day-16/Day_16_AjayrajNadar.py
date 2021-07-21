def create(stack):
    stack = []
def add(stack, a):
    stack.append(a)
def Del(stack):
    stack.pop()
def pr(stack):
    print(stack)
    
s = []
create(s)
add(s, 3)
add(s, 7)
add(s, 4)
Del(s)
add(s, 8)

pr(s)
