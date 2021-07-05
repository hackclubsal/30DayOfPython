# day-4

# Solution
i = int(input("Enter the number of Rows : "))
count = 0

for n in range(1, i+1):
    for j in range(1, n+1):
        print("*", end=" ")
        count += 1
    print("")
print(count, "is total stars in the figure.")
