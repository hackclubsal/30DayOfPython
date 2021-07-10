def sum_natural(num):
    global s
    if num==0:
        s = s + num
    else:
        s = s + num
        return sum_natural(num-1)
    print(f"Sum of natural number is : {s}")

if __name__ == '__main__':
    s = 0
    num = int(input("Enter the number : "))
    sum_natural(num)
