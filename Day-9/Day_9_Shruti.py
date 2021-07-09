import math as m

num = int(input('Enter number'))
print("Last digit of {} is {}".format(num, num % 10))

num = str(num)
length = len(num)

if (length % 2 == 0):
    print(-1)
else:
    mid = m.floor(length/ 2)
    print("Middle digit of {} is {}".format(num, num[mid]))
