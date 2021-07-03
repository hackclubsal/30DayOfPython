# day 3 Solution

# You are given a variable. Write a program to check whether the number is divisible by both 10 and 20.

i = int(input("Enter the number : "))

if(i % 10 == 0 | i % 20 == 0):
    {
        print(i, "is divisible by 10 and 20.")
    }
else:
    {
        print(i, " is either divisible by 10 but not by 20.")
    }
