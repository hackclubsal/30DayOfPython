import numpy as np
m = int(input("Enter number of rows"))
n = int(input("Enter number of column"))
a=[]
l=[]
for i in range(m):
    for j in range(n):
        k = int(input("Enter element"))
        l.append(k)
    a.append(l)
    l=[]
print("Original matrix:")
print(np.matrix(a))
for i in range(m):
    for j in range(n):
        if i > j or i == j:
            continue
        else:
            a[i][j] = 0
print("Lower triangle matrix:")
print(np.matrix(a))
