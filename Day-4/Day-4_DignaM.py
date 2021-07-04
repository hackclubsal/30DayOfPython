# Day-4_Hackclubsal_30DayOfPython_Solution
# Python code to demonstrate star pattern

def pattern(n):
    count = 0
    for n in range(0, n):
        for j in range(0, n+1):
            count += 1
            print("* ", end="")
        print("\r")
    print(f"Number of stars = {count}")
    return 0

n = int(input("Enter the Number of Rows:\n"))
pattern(n)