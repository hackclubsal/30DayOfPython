Number=int(input("Enter Number : " ))
StarCount=0
for i in range(1,Number+1):
    for j in range(1,i+1):
        print("*",end=" ")
        StarCount+=1
    print('\n')   
print("StarCount" ,StarCount)