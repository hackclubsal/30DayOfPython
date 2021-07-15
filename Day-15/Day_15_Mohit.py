# Perform a Quick Sort Algorithm in a Python Program.

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


lst = []
n = int(input("Enter the Elements Range : "))
for i in range(0, n):
    ele = int(input("Element : "))
    lst.append(ele)
print(lst, " are the elemnts.")


quickSort(lst, 0, n-1)
print("Sorted array is:", lst)
