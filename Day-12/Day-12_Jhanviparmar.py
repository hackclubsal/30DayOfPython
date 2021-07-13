#day12
n = int(input("Enter number of digits you want in a list: "))
lst=[]
for i in range(0,n):
    lst.append(int(input("Enter number: ")))
print("List: ",lst)
key = int(input("Enter key number you want to find from list: "))
for j in range(0,len(lst)):
    if key == lst[j]:
        print("Index of given key is: ",j)
    else:
        print("Element not found!")
