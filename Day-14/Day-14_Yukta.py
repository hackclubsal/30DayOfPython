arr = []
n = int(input("Enter the number of elements : "))
for i in range (0,n):
    ele = int(input())
    arr.append(ele)



for i in range (0,n):
    for j in range(0,n-1):
        if(arr[i] < arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)