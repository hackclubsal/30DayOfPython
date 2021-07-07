def numbers(n,m):
    for i in range(n+1,m):
        print(f"{i}, ", end="")
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
print(f"The numbers between {n} and {m} are:")

numbers(n,m)