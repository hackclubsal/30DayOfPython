#day13
n = int(input("Enter number of digits you want in a list: "))
lst=[]
for i in range(0,n):
    lst.append(int(input("Enter number: ")))
print("List: ",lst)
lst.sort()
print("Sorted list: ",lst)

key = int(input("Enter key number you want to find from list: "))
low = 0
high = len(lst)-1

def binarySearch(lst, low, high, key):
    if(high >= low):
        mid = (high + low) // 2
        
        if(lst[mid] == key):
            return mid

        elif (lst[mid] > key):
            return binarySearch(lst, low, mid -1, key)

        else:
            return binarySearch(lst, mid + 1, high, key)
    else:
        return -1

resultIndex = binarySearch(lst, low, high, key )

if resultIndex == -1:
    print("Element not found!!")
else:
    print("Element", key, "found at index", resultIndex)
