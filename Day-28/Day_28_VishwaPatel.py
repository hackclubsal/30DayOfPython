m = int(input('Enter rows'))
n = int(input('Enter columns'))
l = []
b = []
flag = 0
for i in range(0, m):
    l = []
    for j in range(0, n):
        e = input('Enter element: ')
        l.append(e)
    b.append(l)
print(b)

target = input('Enter key to be found')

for i in range(0, m):
    for j in b[i]:
        if(j == target):
            print(True)
            flag = 1 
            break
    if flag == 1:
        break

if flag == 0:
    print(False)
