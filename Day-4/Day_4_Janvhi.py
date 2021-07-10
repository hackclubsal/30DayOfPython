n=int(input("enter number of rows: "))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
count = (n * (n + 1)) / 2
print("stars : ",int(count))
