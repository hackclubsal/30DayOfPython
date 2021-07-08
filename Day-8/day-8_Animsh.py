def addEven(n, m):
    sum = 0
    for i in range(n+1, m):
        if (i % 2 == 0):
            sum += i
    return sum


positive = False
while(positive == False):
    n = int(input("Enter the First number: "))
    m = int(input("Enter the Second number: "))
    if(n < 0 or m < 0):
        print("---------------------------------------------")
        print("Please enter a positive integer only....")
        print("---------------------------------------------")
        continue
    else:
        positive = True
print("----------------------------------------------------------")
print(f"The sum of even numbers between {n} and {m} is: {addEven(n, m)}")


