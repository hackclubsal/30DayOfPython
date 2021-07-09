def lastDigit(a):
    a = str(a)
    return a[len(a)-1]

def advance(a):
    a = str(a)
    if (len(a) % 2 != 0):
        b = int(len(a) / 2)
        return a[b]
    else:
        return -1

a = int(input("Enter your Number: "))
print("---------------------------MAIN----------------------")
print(f"the last digit of {a} is {lastDigit(a)}")
print("---------------------------ADVANCE----------------------")
print(f"The output of Advance is: {advance(a)}")

'''
---------OUTPUT-------------
Enter your Number: 12345
---------------------------MAIN----------------------   
the last digit of 12345 is 5
---------------------------ADVANCE----------------------
The output of Advance is: 3
'''
