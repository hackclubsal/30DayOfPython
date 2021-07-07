c = input('Enter character:')
v = (ord(c))
print("ASCII value:",v)
t = ''
while v >= 1:
    num = int(v % 2)
    t = t + str(num)
    v = v / 2
print("Binary value:", t[::-1])


'''
OUTPUT
Enter character:a 
ASCII value: 97
Binary value: 1100001
'''
