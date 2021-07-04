n = int(input("enter the rows you want to print: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("* ", end="")
    print("\n")
    