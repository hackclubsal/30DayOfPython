# Day-11 Question for the day-11 is --->

# -> Question: Write a Program to print nth Fibonacci number.

# -> Input: Take number as input from the user and store it in a variable.

# -> Output: print the nth Fibonacci number.

# -> Example
# Input: 9
# Output: 34

# Condition: Perform this program without using recursion.

# Expected Time complexity: O(n) 


n=int(input())
t1=0
t2=1
print("nth element of Fibonacci series:",end=" ")
for i in range(1,n):
    t3=t1+t2
    t1=t2
    t2=t3
print(t3)
