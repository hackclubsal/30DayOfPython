# Day-12 Question for the day-12 is --->

# -> Question: Perform a Linear Search Operation in an Array.

# -> Input: Take values of n and k, where n is number of elements in an array and k is the key.

# -> Output: print index position of the key.

# -> Example
# Input: 4, 5
# [2, 4, 5, 8]

# Output: 2
# -> Example
# Input: 6, 3
# [1, 6, 4, 8, 2, 23]

# Output: -1

# (Optional): Try to make it's time complexity better than 0(n). 

# Perform a Linear Search Operation in an Array.

lst = []
n = int(input("Enter the Elements Range : "))
for i in range(0, n):
    ele = int(input(f"{i+1} th Element : "))
    lst.append(ele)
print(lst, " are the elements")

k = int(input("Enter the Number to be find : "))
try:
    ind = lst.index(k)
    print(k, " has the ", ind, "th index in the list)

except:
    print("-1")
    