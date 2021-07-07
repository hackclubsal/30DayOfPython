# Day-5_Hackclubsal_30DayOfPython_Solution
#Program to find out the total number of days in a given month.

l1 = [1,3,5,7,8,10,12]
l2 = [4,6,9,11]
l3 = [2]
n = int(input("Enter Number of month:\n"))
if n in l1:
    print("31 Days")
elif n in l2:
    print("30 Days")
elif n in l3:
    print("28 Days")
else:
    print("Input Valid Month Num !!")

        