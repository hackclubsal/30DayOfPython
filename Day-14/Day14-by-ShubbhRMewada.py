def bubble_sort(l):
    cond=False
    while(cond!=True):
        count=0
        for i in range(len(l)-1):
            if(l[i]>l[i+1]):
                l[i],l[i+1]=l[i+1],l[i]
                count+=1
        if(count==0):
            cond=True
    return l

n=int(input("Enter the Size of your Array:"))
l=[]
for i in range(n):
    l.append(int(input(f"Enter Element number {i+1}: ")))
print(bubble_sort(l))

