import math as m

def last_digit(n):
    n = str(n)
    return int(n[len(n)-1])

n = int(input("Enter Number : "))
print("Last Digit is ",last_digit(n))

length = len(str(n))
if (length % 2 == 0):
    print(-1)
else: 
    mid = m.floor(length/ 2)
    print("Middle digit is ", mid+1)
