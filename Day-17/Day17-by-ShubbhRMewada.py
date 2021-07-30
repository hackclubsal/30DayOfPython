def enqueue(l):
    l.append(int(input("Enter the Value to be inserted : ")))
    print('Insertion Successfull')

def dequeue(l):
    global front
    print(f'Deleting element {l[front]}')
    l.remove(l[front])
    print('Deletion Successfull')

def display(l):
    print('Elements of Your Queue are :')
    for i in l:
        print(i,end=' ')
    print('\n')

l=[]
n=0
front=0
while n!=4 :
    print('PRESS 1 for Entering the Element.')
    print('PRESS 2 for Deleting the Element.')
    print('PRESS 3 for Display of all the Elements.')
    print('PRESS 4 for Exit.')
    n=int(input())
    if n==1:
        enqueue(l)
    elif n==2:
        dequeue(l)
    elif n==3:
        display(l)
    elif n>4:
        print('Please Enter a Valid Input')