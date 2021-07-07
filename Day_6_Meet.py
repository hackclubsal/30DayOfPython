n = input()
print("ASCII Code - ", ord(n))
try:
    a = int(n)
    binary = bin(a)
    print("Binary Code - ", binary[2:])
except:
    pass