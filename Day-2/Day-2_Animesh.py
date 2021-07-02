def cube(a):
    if a>0:
        return a**(1/3)
    else:
        return -(-a)**(1/3)

a = int(input("Enter any number to find cube root of: "))
print(f"the cude root {a} is {cube(a)}")