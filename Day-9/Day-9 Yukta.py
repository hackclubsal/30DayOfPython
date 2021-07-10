import math
x = int(input("Enter a number : "))
y = x % 10
print("Last digit of given number is : ",y)
# ADVANCE SOLUTION -- 
string_convert = str(x)
length = len(string_convert)

if(length % 2 == 0):
    print(-1)
else:
    median = int((x // math.pow(10, length // 2))) % 10;
    print(median)
    
