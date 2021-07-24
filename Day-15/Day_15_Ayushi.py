# Day-15 Question for the day-15 is --->

# -> Question: Perform a Quick Sort Algorithm in a Python Program.

# -> Input: N, arr[ ]
# N- is number of elements in an array.

# -> Output: print sorted array.

# -> Example
# Input: 4, [4, 1, 3, 9, 7]

# Output: [1, 3, 4, 7, 9]


# -> Example

# Input: 10, [4, 3, 45, 11, 6, 86, 65, 23, 90, 55]

# Output: [3, 4, 6, 11, 23, 45, 55, 65, 86, 90]


n = int(input('Enter number of elements: '))
arr = []

for i in range (0, n):
    x = int(input('Enter element: '))
    arr.append(x)
    
def partition(arr, low, high):
    i = (low-1)        
    pivot = arr[high]    
  
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
    
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
        
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

quickSort(arr, 0, n - 1)
print(arr)
