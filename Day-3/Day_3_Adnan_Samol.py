#Day-3

n = int(input("Enter the number:"))

def isDivisible(n):
    if(n%10== 0 and n%20==0 ):
        return str(n) + " is divisible by both 10 & 20."
    else:
        return  str(n) + " is not divisible by both 10 & 20"

print(isDivisible(n));
