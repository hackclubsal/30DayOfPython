n=int(input("Enter the starting value n : "))
m=int(input("Enter the ending value m : "))
for i in range(n+1,m):
    if (n>0 and m>n):
        print(i,end=" ")
    else:
        print("Please enter n>0 or m>n")
        break