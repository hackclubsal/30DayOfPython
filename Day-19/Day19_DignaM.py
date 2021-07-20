# Day-19_Hackclubsal_30DayOfPython_Solution
# Remove Duplicates from the given array and also print duplicate number.

list1=[]

size = int(input("Enter size of array : "))

for i in range(0,size):
    x = int(input("Enter element : "))
    list1.append(x)
print(list1)

list2=[]

for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        print("Duplicate Element : ",i)
print(list2)

