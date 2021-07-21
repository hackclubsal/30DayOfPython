from collections import Counter
arr = []
fin = []
flag = 0
n = int(input("Enter the number of elements to enter : "))
for i in range(0, n):
    ele = int(input())
    arr.append(ele)

print("Original array : ", arr)
fin = list(dict.fromkeys(arr))
print("Final array is :", fin)
d = Counter(arr)
dup = list([item for item in d if d[item] > 1])
print("Duplicate values : ", dup)