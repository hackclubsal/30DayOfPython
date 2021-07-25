# Day-8 Question for the day-8 is --->

# -> Question: Write a program to print the sum of all the even numbers between n and m ( n and m are user input).

# -> Input: Take  two number as input from the user and store it in a variables.

# -> Output: print the sum of all even number between n and m.

# -> Example
# Input: n=0,m=10
# Output: 20

n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))
sum=0
for i in range(n+1,m):
    if i%2==0:
        sum+=i
print("Sum: ",sum)
