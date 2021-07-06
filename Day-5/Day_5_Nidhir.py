a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
c = [2]
n = int(input("Enter Number of month:"))
if n in a:
    print("31 Days")
elif n in b:
    print("30 Days")
elif n in c:
    print("28 Days")
else:
    print("Month should be between 1 to 12")
