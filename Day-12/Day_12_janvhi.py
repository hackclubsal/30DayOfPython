n= int(input("enter numbers of elements:"))

a=[]
flag=0
for i in range(0,n):
        x = int(input("enter element"))
        a.append(x)
print(a)


k= int(input("enter no to be searched"))
def LinearSearch(k,a):
    if k in a:
        print("index found at",k, "is", a.index(k))
    else:
            print("element not found")
LinearSearch(k,a)
