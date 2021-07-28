# Given a matrix of size m*n. Search for a value in this m*n matrix.
m=int(input("Enter number of rows"))
n=int(input("Enter number of columns"))
l=[]
a=[]
flag=0
for i in range(0,m):
    for j in range(0,n):
        k=int(input("Enter element"))
        l.append(k)
    a.append(l)
    l=[]
print(a)
y=int(input("enter element you want to search"))
for i in range(0, m):
    for j in a[i]:
        if (j == y):
            print(True)
            flag = 1
            break
    if flag==1:
        break

if flag == 0:
    print(False)
