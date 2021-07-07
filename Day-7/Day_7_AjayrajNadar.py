n = int(input("Enter n: "))
m = int(input("Enter m: "))

if n > 0 and m > 0 and n>m:
    print("Wrong input!!!")
else:
    for i in range(n+1,m):
        print(i, end = ' ')