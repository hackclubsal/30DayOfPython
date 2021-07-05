#Day-3 Challenge

#-> Question: You are given a variable. Write a program to check whether the number is divisible by both 10 and 20. 

#-> Input: Take input from the user and store it into the variable.
#-> Output: Print a statement whether the number is divisible by both 10 & 20.

#-> Example
#Input:40
#Output:yes, 40 is divisible by both 10 & 20.


a=int(input())
if(a%20==0 and a%10==0):
    print(f"Yes! {a} is divisible by both 10 and 20")
else:
    print(f"No! {a} is not divisible by both 10 and 20")