n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))
sum=0
for i in range(n+1,m):
    if i%2==0:
        sum+=i
print("Sum: ",sum)
