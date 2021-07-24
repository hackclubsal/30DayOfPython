# Day-19 Question for the day-19 is --->

# -> Question: Remove Duplicates from the given array and also print duplicate number.

# -> Input: 
# 6, [5, 7, 4, 7, 2, 3]

# -> Output: 
# 7

n = int(input('Enter number of elements: '))
l = []

for i in range (0, n):
    x = int(input('Enter element: '))
    l.append(x)

freq = {}
for item in l:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1

for key, value in freq.items():
    if (value != 1):
        print(key)

l = set(l)
