from bisect import bisect_left
  
def BinarySearch(arr, n):
    i = bisect_left(arr, n)
    if i != len(arr) and arr[i] == n:
        return i
    else:
        return -1
  
arr  = []

n = int(input("Enter number of elements : "))


for i in range(0, n):
    ele = int(input())
 
    arr.append(ele) 





k = int(input("Enter the element to be searched : ")) 

res = BinarySearch(arr, k)
if res == -1:
    print(k, "is absent")
else:
    print("First occurrence of", k, "is present at", res+1)

