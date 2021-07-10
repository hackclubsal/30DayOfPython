# Write a program that returns the last digit in a number.
import math
i = int(input("Enter the Number : "))
y = 0
for x in range(len(str(i))):
    if i > 10:
        y = i % 10

print(y, "is the last digit of the number.")

# Function to find the middle digit


def middleDigit(n):
    digits = math.log10(n) + 1
    n = int((n // math.pow(10, digits // 2)) % 10)
    return n


if (len(str(i)) % 2 != 0):
    print(middleDigit(i), "is the middle digit of the Number.")
else:
    print("Your number has even digit in the number.")
