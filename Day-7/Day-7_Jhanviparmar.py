#day7
n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))
if(n<0 or m<0):
    print("Please enter non-negative numbers")
else:
    for i in range(n+1,m):
        print(i)
