print("Enter positive numbers : ")
n = int(input("Enter starting range : "))
m = int(input("Enter ending range : "))
if(n > m):
    print("Wrong input!")
else:
    for i in range(n+1,m):
        print(i, end=' ')