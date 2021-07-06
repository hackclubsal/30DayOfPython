l1 = [1,3,5,7,8,10,12]
l2 = [4,6,9,11]
l3 = [2]
n = int(input("Enter number of month: "))
if n in l1:
    print("31 Days")
elif n in l2:
    print("30 Days")
elif n in l3:
    print("28 Days")
else:
    print("input n less than 13")