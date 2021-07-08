n=int(input("enter starting range"))
m=int(input("enter ending range"))
x=0
for i in range(n+1,m):
    if i%2==0:
       x=x+i
print("sum of even nos. in given range is",x)
