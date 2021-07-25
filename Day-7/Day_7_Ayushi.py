# Day-7 Question for the day-7 is --->

# -> Question: Write a program to print all the natural numbers between n and m (Where n and m are user input and n>0, m>0)

# -> Input: Take  two number as input from the user and store it in a variables.

# -> Output: print all natural numbers between n and m.

# -> Example
# Input: n=1,m=6
# Output: 2,3,4,5

n=int(input())
m=int(input())
for i in range(n+1,m):
    print(i,end=",")
