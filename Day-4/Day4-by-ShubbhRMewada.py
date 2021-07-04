# Without List comprehension
n=int(input('Enter the Number of Rows: '))
count=0
for i in range(1,n+1):
    l=['*']*i
    count+=i
    str=''
    str=str.join(l)
    print(str)
print(count)

# With List comprehension
l=[['*']*i for i in range(1,int(input("Enter the Number of Rows: "))+1)]
count=0
for i in l:
    str=''
    str=str.join(i)
    count+=len(i)
    print(str)
print(count)