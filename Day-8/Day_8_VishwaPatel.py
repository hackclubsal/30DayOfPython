n = int(input("Enter starting range"))
m = int(input("Enter ending range"))

sum = 0
for i in range (n + 1, m):
    if (i % 2 == 0):
        sum = sum + i

print("Sum of even numbers between {} and {} is: {}".format(n, m, sum))
