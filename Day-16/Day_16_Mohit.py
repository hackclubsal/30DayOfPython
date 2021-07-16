# Implement a Stack in Python. Also perform Push and Pop Operations.

lst = []
i = int(input("Enter the lenth of the Stack : "))

def fun(i, lst):
    k = input("enter your choice to do operation push or pop : ")
    for n in range(0, i+1):
        if (k == "push"):
            ele = int(input("Element : "))
            lst.append(ele)
            fun(0, lst)
        elif k == "pop":
            lst.pop()
            fun(0, lst)
        else:
            print(lst, " are the elemnts.")
            exit()


fun(i, lst)
