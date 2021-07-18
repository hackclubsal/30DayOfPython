# Implement a Queue in Python. Also perform Enqueue and Dequeue Operations.

lst = []
i = int(input("Enter the lenth of the Queue : "))


def fun(i, lst):
    k = input("enter your choice to do operation Enqueue or Dequeue : ")
    for n in range(0, i+1):
        if (k == "enqueue"):
            ele = int(input("Element : "))
            lst.append(ele)
            fun(0, lst)
        elif k == "dequeue":
            lst.remove(lst[0])
            fun(0, lst)
        else:
            print(lst, " are the elemnts.")
            exit()


fun(i, lst)
