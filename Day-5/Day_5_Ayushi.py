# Day-5 Question for the day-5 is --->

# -> Question: Write a program to find out the total number of days in a given month.
# -> Input: Take n which is number of the month
# -> Output: print number of days in the given month.

# -> Example
# Input: 6 (June)
# Output: 31

# Condition: Assume that there is no leap year involved and Feb days are 28.
# Advance:Try to Implement with HashMap (not for beginners)

list1 = [1, 3, 5, 7, 8, 10,12]
list2 = [4, 6, 9, 11]
list3 = [2]
Month = int(input("Enter the Month Number : "))
if Month in list1:
    print(31)
elif Month in list2:
    print(30)
elif Month in list3:
    print(28)
else:
    print("Please enter below 13 month")

# or

if __name__ == "__main__":
    def getDate(a):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        print(f"There are {days[a-1]} days in the month of {months[a-1]}")
        return 0

    a = int(input("Enter the month in integer: "))
    getDate(a)
