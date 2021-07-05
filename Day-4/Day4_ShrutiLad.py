count=0
x=int(input("enter no. of rows"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print("*",end="")
        count+=1
    print("\n")
print("no.of stars=",count)
