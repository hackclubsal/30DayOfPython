n,m=[int(x) for x in input().split()]

evensum=0
if(n%2):
    n-=1
if(m%2):
    m+=1
temp=n    
if(n==m or n>m):
    print(0)
else:
    while(n<=m):
        evensum+=n
        n+=2
    n=temp    
    print(evensum-n-m)    
        