n=input("Enter a character to find it's ASCII code: ")
p=ord(n)
l=[]
print(f'The ASCII code of {n} is :',p)
while(p>0):
    l.append(p%2)
    p=p//2
print(f'Binary of ASCII of {n} is : ',end='')
for i in l:
    print(i,end='')