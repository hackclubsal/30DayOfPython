#day19
list=[]
n=int(input("Enter size of list: "))
for i in range(0,n):
    list.append(int(input("Enter element: ")))

listCopy=[]
for i in list:
    if i not in listCopy:
        listCopy.append(i)
    else:
        print(i,end=' ')
print(listCopy)
