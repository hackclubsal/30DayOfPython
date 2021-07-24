# Day-13 Question for the day-13 is --->

# -> Question: Perform a Binary Search Operation in an Array.

# -> Input: Take values of n and k, where n is number of elements in an array and k is the key.

# -> Output: print index position of the key.

# -> Example
# Input: 4, 5
# [2, 4, 5, 8]

# Output: 2

# -> Example

# Input: 6, 3
# [1, 6, 4, 8, 2, 23]

# Output: Element not found



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

k = int(input("Enter the number to be found : "))

result = binarySearch(lst, 0, len(lst)-1, k)

if result != -1:
    print("Element is present at index ", result)
else:
    print("Element is not present in array")
