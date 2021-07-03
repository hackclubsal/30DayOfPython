# day 2

i = int(input("Enter the number : "))


def cube_root(x):
    if (x >= 0):
        return round(x**(1/3))
    else:
        return round(-(-x)**(1/3))


print(cube_root(i), "is the answer")
