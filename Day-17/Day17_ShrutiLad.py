print("Enter  (1) for insert (2) for delete (3) for print (4) for exit")
Queue=[]
def ENQUEUE(x):
    Queue.append(x)

def DEQUEUE():
    try:
        print("Element ",Queue.pop(0)," is popped")
    except:
        print("No elements here")

def pr_Queue():
    print(Queue)

n=0

while(n!=4):
    
    n=int(input("Enter command no."))
    if(n==1):
        x=int(input("Enter element"))
        ENQUEUE(x)
    elif(n==2):
        DEQUEUE()
    elif(n==3):
        pr_Queue()
    elif(n==4):
        print("Bye!!!")
        break
