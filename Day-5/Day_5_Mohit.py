# Write a program to find out the total number of days in a given month.

i1 = [1, 3, 5, 7, 8, 10, 12]
i2 = [4, 6, 9, 11]
i3 = [2]

i = int(input("Enter the number of month : "))


def Days(i):
    if i in i1:
        print(i, "has the total 31 DAYS in the month.")
    elif i in i2:
        print(i, "has the total 30 DAYS in the month")
    else:
        print(i, "has the total 28 DAYS in the month")


Days(i)
