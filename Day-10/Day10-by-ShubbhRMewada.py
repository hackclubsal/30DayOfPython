import time
# Using time module to compare the Time Taken by Each program

# Best Case Possible---
# Used arithmetic progression.
# For N->infinity, Feasible
c=time.time()
sum=0
n=int(input("Enter A Natural Number: "))
print(n*(n+1)//2)
d=time.time()
print(f'Time taken by the above mentioned program is {d-c} seconds')

# Mediocre Case Possible----
# Good for Small values but for N -> infinity, not feasible
print()
e=time.time()
sum1=0
for i in range(n+1):
    sum1+=i
print(sum1)
g=time.time()
print(f'Time taken by the above mentioned program is {g-e:.10f} seconds')

# Mediocre Case Possible----
# Good for Small values but for N -> infinity, not feasible
a=time.time()
l=[i for i in range(int(input("Enter A Natural Number: "))+1)]
print(sum(l))
b=time.time()
print(f'Time taken by the above mentioned program is {b-a} seconds')