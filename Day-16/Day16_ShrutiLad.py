print("Enter  (1) for push (2) for pop (3) for print (4) for exit")
stack=[]
def push_opp(x):
    stack.append(x)

def pop_opp():
    try:
        print("Element ",stack.pop()," is popped")
    except:
        print("No elements here")

def pr_stack():
    print(stack)

n=0

while(n!=4):
    
    n=int(input("Enter command no."))
    if(n==1):
        x=int(input("Enter element"))
        push_opp(x)
    elif(n==2):
        pop_opp()
    elif(n==3):
        pr_stack()
    elif(n==4):
        print("Bye!!!")
        break
