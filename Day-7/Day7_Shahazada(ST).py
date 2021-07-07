n=0
m=0
while( n<=0 or m<=0):
    n,m=input("Enter two number both should be >0:-").split()
    n=int(n)
    m=int(m)
    
    if(n<=0 or m<=0):
        print('Both number should be >0')

if(n==m or n>m or m-n==1):
    print('NO Natural Number between both number')
else:    
    n+=1
    while(n<m):
        if(n+1==m):
            print(n)
        else:    
            print(n,end=',')
        n+=1    
    
    
