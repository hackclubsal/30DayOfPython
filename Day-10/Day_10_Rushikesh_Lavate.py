# method 1: using inbuilt function
def sum_nat_1(num):
    s = sum(range(num+1))
    print("Sum of natural number using inbuilt function is : ",s)

# method 2: using mathematical formula
def sum_nat_2(num):
    s = int((num*(num+1))/2)
    print("Sum of natural number using mathematical formula is : {}".format(s))

# method 3: using recursion
# default recursion limit is 1000, it means that function call on itself only 1000 times
# we can set it our own limit using below code
import sys
sys.setrecursionlimit(999999)

def sum_nat_3(num):
    global s
    if num==0:
        s = s + num
    else:
        s = s + num
        return sum_nat_3(num-1)
    print(f"Sum of natural number using recursion is : {s}")


if __name__ == '__main__':
    s = 0
    num = int(input("Enter the number : "))
    sum_nat_1(num)
    sum_nat_2(num)
    sum_nat_3(num)
