#day5
list1 = [1,3,5,7,8,10,12]
list2 = [4,6,9,11]
list3 = [2]
n = int(input("Enter number of month: "))
if n in list1:
    print("31 Days")
elif n in list2:
    print("30 Days")
elif n in list3:
    print("28 Days")
else:
    print("Please enter n having value less than 13")
