# Write a Program to print nth Fibonacci number.

i = int(input("Enter the number : "))

n1, n2 = 0, 1
count = 0

if i > 0:
    if i == 1:
        print("Fibonacci sequence of", i, "th number is :", n1)
    else:
        while count < i:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

print("Fibonacci sequence of ", i, "th number is :", n1)
