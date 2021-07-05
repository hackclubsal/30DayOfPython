l1=[1,3,5,7,8,10,12]
l2=[4,6,9,11]
l3=[2]
i=int(input("enter month"))
if i in l1:
    print("31")
elif i in l2:
    print("30")
elif i in l3:
    print("28")
else:
    print("enter valid month")
