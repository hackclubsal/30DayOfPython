# Write a program to print the sum of all the even numbers between n and m ( n and m are user input).

n = int(input("Enter the First Number of the Range : "))
m = int(input("Enter the Last Number of the Range : "))
x = 0
for i in range(n+1, m):
    if (i % 2 == 0):
        x = x + i

print(x, " is the total sum of even numbers.")
