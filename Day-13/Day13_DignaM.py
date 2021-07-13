n = int(input("Enter number of elements: \n "))
arr = []

for i in range (0, n):
    x = int(input('Enter element: '))
    arr.append(x)
arr.sort()

k = int(input('Enter the element you want to search: '))
low = 0
high = len(arr) - 1

def binarySearch(arr, low, high, k):
    if(high >= low):
        mid = (high + low) // 2
        if(arr[mid] == k):
            return mid
        elif (arr[mid] > k):
            return binarySearch(arr, low, mid -1, k)
        else:
            return binarySearch(arr, mid + 1, high, k)
        else:
            return -1
result = binarySearch(arr, low, high, k )

if result == -1:
    print("Element not found")
else:
    print("Element", k, "found at index", result)
    
    