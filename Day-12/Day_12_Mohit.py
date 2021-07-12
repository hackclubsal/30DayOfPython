# Perform a Linear Search Operation in an Array.

lst = []
n = int(input("Enter the Elements Range : "))
for i in range(0, n):
    ele = int(input("Element : "))
    lst.append(ele)
print(lst, " are the elemnts.")

k = int(input("Enter the Number to be find : "))

ind = lst.index(k)

print(k, " has the ", ind, "th index in the list which is ", lst, ".")
