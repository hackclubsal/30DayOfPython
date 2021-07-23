#day23
arr=[]
n = int(input("Enter the size of array: "))
for i in range(0,n):
    arr.append(int(input("Enter Elements: ")))
arr1=[]
x = arr[-2]
y = arr[-1]
arr1.append(x)
arr1.append(y)
for i in range(0,len(arr)-2):
    arr1.append(arr[i])
print(arr1)

#input:n=5,arr=[1,2,3,4,5]
#output:[4,5,1,2,3]
