n = int(input())
m = int(input())
for i in range(n+1,m):
    if i == m-1:
        print(i)
    else:
        print(i, end=",")