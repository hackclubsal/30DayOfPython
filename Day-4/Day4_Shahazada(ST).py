num=int(input())


i=1
while(i<=num):
    j=1
    while(j<=i):
        print('*',end=' ')
        j+=1
    print() 
    i+=1
print(int((num*(num+1))/2))  



# By  single Loop  


for i in range(1,num+1):
    print("* "*(i))
print((num*(num+1))//2) #without explicitly int conversion   
