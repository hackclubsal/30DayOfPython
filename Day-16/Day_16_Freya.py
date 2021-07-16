# implementation of stack
l=[]
while (1):
    print("1: Push\n 2:Pop\n 3:Print stack\n 4:Break")
    x = int(input("enter your choice"))
    if x==1:
        y=input("enter element you want to add")
        l.append(y)
    elif x==2:
        try:
         l.pop()
         print("element poped is",l.pop())
        except:
         print("list is empty")
    elif x==3:
        print(l)
    elif x==4:
        break
    else:
        print("enter valid number")


