#Day-2
a = float(input("Enter the number to find cube root:"))
def cubeRoot(a):
    if(a == 0):
        return 0;
    else:
        return (a**(1/3))   

print("The cube root of",int(a), "is",cubeRoot(a))
