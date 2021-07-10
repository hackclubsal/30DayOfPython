#Day-9_Hackclubsal_30DayOfPython_solution
#program that returns the last digit in a number.

num  = int(input("Enter Num : \n"))
lastDigit = num % 10 
print("Lat Digit Of number is :",lastDigit)

#Advance Problem Solution
import math
def middleDigit(num):
    
    digits = math.log10(num) + 1;
    if (len(str(abs(num))) % 2) != 0:  
         n = int((num // math.pow(10, digits // 2))) % 10;
         return n;
    else:
        return -1;

mid_digit=(middleDigit(num))
print("Middle Digit Of Number is :",mid_digit)