#day19_challenge
l=[]
n=int(input("enter size of array"))
for i in range(0,n):
    x=int(input("enter element"))
    l.append(x)

l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')
l=set(l)
print(list(l))
