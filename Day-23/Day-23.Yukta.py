def cycrot(arr,n):
 
    i = 0
    j = n - 1
    while i != j:
      arr[i], arr[j] = arr[j], arr[i]
      i = i + 1
    pass

arr = []
n = int(input("Enter the range of array :"))
for i in range (0,n) :
    ele = int(input())
    arr.append(ele)
print("Original array :", arr)

cycrot(arr,n)
cycrot(arr,n)

print("After 2 cyclic rotations array becomes :", arr)
