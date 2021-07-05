l1=[1,3,5,7,8,10,12]
l2=[4,6,9,11]
month={i:31 if i in l1 else 30 for i in range(1,12) }
month[2]=28
n=int(input("Enter the Name of the Month:"))
print(month[n])