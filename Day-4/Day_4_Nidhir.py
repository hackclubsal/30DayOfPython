n=int(input("Enter value of pyramid :"))
total_star=(n*(n+1)/2)
for x in range(0,n):
    for i in range(0,x+1):
        print("*",end="")
    print()
print("The total no. of * is ",total_star)


