def push (l):
    n=int(input("Please Enter an element to Insert: "))
    l.append(n)
    print('Insertion Successfull')

def pop(l):
    if l:
        l.pop()
        print('Deletion Successfull')
    else:
        print('List is Empty \nPlease try to Insert some values')

def display(l):
    if l:
        print('Your List Contains:')
        for i in l:
            print(i,end=' ')
        print('\n')
    else:
        print('List is Empty \nPlease try to Insert some values')

l=[]
n=0
while n!=4 :
    print('PRESS 1 for Entering the Element.')
    print('PRESS 2 for Deleting the Element.')
    print('PRESS 3 for Display of all the Elements.')
    print('PRESS 4 for Exit.')
    n=int(input())
    if n==1:
        push(l)
    elif n==2:
        pop(l)
    elif n==3:
        display(l)
    else:
        print('Please Enter a Valid Input')
