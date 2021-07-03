# 30 Days of Python Hackclub SAL- Rajdeep Das
# Python Program to Check Number is Divisible by 10 and 20

number = int(input(" Please Enter any Positive Integer : "))

if((number % 10 == 0) and (number % 20 == 0)):
    print("Given Number {0} is Divisible by 10 and 20".format(number))
else:
    print("Given Number {0} is Not Divisible by 10 and 20".format(number))
    
    
    
#-----------------output------------------------------------------------------------------------------

#Please Enter any Positive Integer : 40
#Given Number 40 is Divisible by 10 and 20

#Please Enter any Positive Integer : 30
#Given Number 30 is Not Divisible by 10 and 20

#Please Enter any Positive Integer : 100
#Given Number 100 is Divisible by 10 and 20

#Please Enter any Positive Integer : 90
#Given Number 90 is Not Divisible by 10 and 20

