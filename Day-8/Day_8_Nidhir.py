n=int(input("Enter the starting Integer"))
m=int(input("Enter the ending Integer"))
x=0
for i in range(n+1,m):
    if i%2==0:
        x=x+i
print(x)