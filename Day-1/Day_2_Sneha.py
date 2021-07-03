a= int(input())
for i in range(2,a):
    count=0
    if a%i==0:
        while count!=3:
            a=a/i
            count+=1
            if a==1:
                print(i)