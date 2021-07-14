#binary search 
n=int(input("enter size of array"))
a=[]
for i in range(0,n):
    x=int(input("enter element"))
    a.append(x)
a.sort()
print(a)
y=int(input("enter element you want to search"))
def binary_search(a,y):
    low=0
    high=len(a)-1
    mid=0
    while low<=high:
        mid=(high+low)//2

        if a[mid]<y:
            low=mid+1

        elif a[mid]>y:
            high=mid-1

        else:
            return mid
    return -1
res=binary_search(a,y)
if res !=-1:
    print("Element present at index",res)
else:
    print("Element is not present in array")
