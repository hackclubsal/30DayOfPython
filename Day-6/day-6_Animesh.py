def ascii(a):
    return ord(a)

def binaary(a):
    b = ''.join(format(ord(i), '08b') for i in a)
    return str(b)
def code(a):
    print(f"The ASCII value of {a} is {ascii(a)}")
    print(f"The Binary value of {a} is {binaary(a)}")

if __name__ == "__main__":
    a = input("Enter any character to find it's ASCII code: ")
    code(a)        
    
        
