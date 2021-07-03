def divByTen(a):
    if (a % 10 == 0):
        print(f"{a} is divisible by 10")
        return 0
    else:
        print(f"{a} is not divisible by 10")

def divByTwenty(a):
    if (a % 20 == 0):
        print(f"{a} is divisible by 20")
        return 0
    else:
        print(f"{a} is not divisible by 20")

a = int(input("ENter a number: "))

def main(a):
    divByTen(a)
    divByTwenty(a)
main(a)
