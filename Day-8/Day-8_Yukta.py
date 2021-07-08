n = int(input("Enter starting range : "))
m = int(input("Enter ending range : "))
sum =0
if(n > m):
    print("Wrong input!")
else:
    for i in range(n+1,m):
        if(i % 2 == 0):
            sum = sum + i
        
        
    print("Sum : ",sum)
'''
OUTPUT-
Enter starting range : 0
Enter ending range : 10
Sum :  20
'''