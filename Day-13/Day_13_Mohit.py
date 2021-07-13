# Perform a Binary Search Operation in an Array.

def binarySearch(arr, l, r, x):  # l is starting part and r as it is ending of the range

    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        return -1


lst = []
n = int(input("Enter the Elements Range : "))
for i in range(0, n):
    ele = int(input("Element : "))
    lst.append(ele)
print(lst, " are the elemnts.")

k = int(input("Enter the Number to be find : "))

result = binarySearch(lst, 0, len(lst)-1, k)

if result != -1:
    print("Element is present at index ", result)
else:
    print("Element is not present in array")
