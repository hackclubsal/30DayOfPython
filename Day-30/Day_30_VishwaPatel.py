import numpy as np
m = int(input('Enter rows'))
n = int(input('Enter columns'))
l = []
b = []
for i in range(m):
    l = []
    for j in range(n):
        e = int(input('Enter element: '))
        l.append(e)
    b.append(l)
print("Original matrix")
print(np.matrix(b))

for i in range(m):
    for j in range(n):
        if i > j or i == j:
            continue
        else:
            b[i][j] = 0

print("Changed matrix")
print(np.matrix(b))
