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
    print("please enter below 13 month")
