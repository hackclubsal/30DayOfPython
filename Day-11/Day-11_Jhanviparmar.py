#day11
n = int(input("Enter a number: "))
c = 0
a,b = 0, 1
list = [a, b]
for i in range(2,n+1):
    c = a+b
    list.append(c)
    a,b = b, c
print(n,"th fibonacci number is ",list[n])
