# Write a program to find ascii code of the given input character.

i = input("Enter the value whose ASCII value you want to know : ")

print(ord(i), "is the ASCII value of ", i, ".")


def convertToBinary(n):
    if n > 1:
        convertToBinary(n//2)
    print(n % 2, end='')


dec = ord(i)
convertToBinary(dec)
print(" is the binary conversion of ", i, "'s ASCII value.")
