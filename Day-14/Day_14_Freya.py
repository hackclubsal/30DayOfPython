#bubble sort
n=int(input("enter size of array"))
a=[]
for i in range(0,n):
    x=int(input("enter element"))
    a.append(x)
print("Before sorting:",a)

def bubble_sort(a):
    n = len(a)
    for i in range (0,n-1):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

bubble_sort(a)
print("After sorting:",a)
