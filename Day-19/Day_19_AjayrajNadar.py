n = int(input('Enter number: '))
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
print(list(l))
