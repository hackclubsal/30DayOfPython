#day20
str = input("Enter a string: ")
print(str)
str = str.split()
for i in range(0,len(str)):
    result = str[i].capitalize()
    print(result, end=" ")
