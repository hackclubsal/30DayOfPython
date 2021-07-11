n = int(input('Enter number'))
a = 0
b = 1 
c = a + b

for i in range(1, n-1):
    a = b
    b = c 
    c = a + b
print("The {}th element in Fibonacci series is {}".format(n, c))
