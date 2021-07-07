c = input("Enter the character: -")
print("The ASCII value of '" + c + "' is", ord(c))

b = bin(int.from_bytes(c.encode(), 'big'))
print("The Binary of ASCII number of '" + str(ord(c)) + "' is :-",b)

