#day15
arr = []
n=int(input("Enter size of array: "))
for i in range(0,n):
    x=int(input("enter no."))
    arr.append(x)
print("Array: ",arr)

def partition(start, end, array):
    pivotIndex = start
    pivot = array[pivotIndex]
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if(start < end):
            array[start], array[end] = array[end], array[start]
    array[end], array[pivotIndex] = array[pivotIndex], array[end]
    
    return end
     
def quick_sort(start, end, array):
     
    if (start < end):
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
         
quick_sort(0, len(arr) - 1, arr)
print("Sorted array: ",arr)
