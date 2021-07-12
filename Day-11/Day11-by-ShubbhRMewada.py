n1=0
n2=1
l=[n1,n2]
n=int(input("Enter nth Number to find the corresponding Fibbonacci Number: "))
for i in range(2,n):
    l.append(l[i-1]+l[i-2])
print(f'Hence the value of {n}th Fibbonacci Number is {l[n-1]}')