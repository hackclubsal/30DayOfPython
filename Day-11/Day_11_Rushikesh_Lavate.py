# default recursion limit is 1000, it means that function call on itself only 1000 times
# we can set it our own limit using below code
import sys
sys.setrecursionlimit(999999)

#method 1 :
def fibonacci_1(num):
    if num < 0:
        return ('Number must be greater than 0')
    elif num==0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci_1(num-1) + fibonacci_1(num-2)

# method 2:
def fibonacci_2(num):
    global f0, f1
    if num < 0:
        return ('Number must be greater than 0')
    else:
        if num== 0:
            return f0
        else:
            f0, f1 = f1, f0+f1
            return fibonacci_2(num-1)

if __name__ == '__main__':
    f0, f1 = 0, 1
    num = int(input("Enter the number : "))
    print("Fibonacci element at {} position is : {}".format(num,fibonacci_1(num)))
    print(f"Fibonacci element at {num} position is : {(fibonacci_2(num))}")
