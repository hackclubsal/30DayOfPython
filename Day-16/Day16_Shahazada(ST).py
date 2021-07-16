def stackPop(stack):
    if(len(stack)==0):
        print('Stack is empty')
    else:
        print('Poped element is: {} '.format(stack[-1]))
        stack.pop()
        print('stack after pop {}'.format(stack))
        print()

def stackPush(stack,ele):
    print('Push element is : {} '.format(ele))
    stack.append(ele)
    print('stack after push : {}'.format(stack))
    print()
    
if __name__ == '__main__':
    stack=[]
    
    pushpop=int(input('want to implement  push/pop enter 1 otherwise 0'))
    while(pushpop):
        push=int(input('Want to push element into stack enter 1 other wise 0:- '))
        if(push):
            ele=input('Enter element you want to push into stack:- ')
            stackPush(stack,push)
        print()
        
        pop=int(input('Want to pop element into stack enter 1 other wise 0:- '))
        if(pop):
            stackPop(stack)
        pushpop=int(input('want to implement more pushpop enter 1 other wise 0:- '))
        print()    
    
    print("Final stack {}".format(stack))
