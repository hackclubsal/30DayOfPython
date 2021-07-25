#day25
'''arr=[]
n = int(input("Enter the size of array: "))
for i in range(0,n):
    arr.append(int(input("Enter Elements: ")))
target=int(input("Target: "))'''
arr=[2,7,11,15]
target=9
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print("(",i ,",",j,")")
