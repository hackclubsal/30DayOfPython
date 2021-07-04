#day4
n = int(input("Enter a number :"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*", end="")
    print("\n")
star_count = (n*(n+1))/2
print("Total stars : ",int(star_count))
