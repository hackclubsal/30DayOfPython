x = int(input("Enter a number : "))
count = 0
for i in range(0,x):
    for j in range(0,i+1):
        print("* ",end ="")
        count +=1
    print()
print(count)
