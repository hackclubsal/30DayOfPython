# 30 Days of Python- Rajdeep Das
# Python Program to Check Number is Divisible by 10 and 20

number = int(input(" Please Enter any Positive Integer : "))

if((number % 10 == 0) and (number % 20 == 0)):
    print("Given Number {0} is Divisible by 10 and 20".format(number))
else:
    print("Given Number {0} is Not Divisible by 10 and 20".format(number))
