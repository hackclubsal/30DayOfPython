#Day 2 Challenge

#-> Question: You are given a variable a. Write a program to find the cube root of a number.

#-> Input: Take input from the user and store it into the given variable.
#-> Output: Print the cube root of the number stored in variable a.

#-> Example
#Input: a = 125
#Output: 5. 


import math
a=int(input())
if a>=0:
    print(f"Cube root of {a} is {a**(1/3)}")
    print(f"Cube root of {a} upto 3 decimal places is {round(a**(1/3),3)}")
    print(f"Cube root of {a} in ceiling form is {math.ceil(a**(1/3))}")
if a<0:
    print(f"Cube root of {a} is {-(-a)**(1/3)}")
    print(f"Cube root of {a} upto 3 decimal places is {round(-(-a)**(1/3),3)}")
    print(f"Cube root of {a} in ceiling form is {math.ceil(-(-a)**(1/3))}")