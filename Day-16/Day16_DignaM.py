# Day-16_Hackclubsal_30DayOfPython_Solution
# Program to Implement a Stack in Python

def createStack(stack):
    stack = []
def push(stack, a):
    stack.append(a)
def pop(stack):
    stack.pop()
def display(stack):
    print(stack)
s = []
createStack(s)
push(s, 3)
push(s, 7)
push(s, 4)
pop(s)
push(s, 8)
display(s)
