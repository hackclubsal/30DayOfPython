# Day-10_Hackclubsal_30DayOfPython_Solution
# Program to find sum of N natural numbers

# Using built-in function sum()
n = int(input("Enter number"))
ans = sum(range(1, n + 1))
print("Sum : ", ans)

# Using Formula
n = int(input("Enter number"))
ans = n * (n + 1) / 2
print('Sum :', int(ans))
