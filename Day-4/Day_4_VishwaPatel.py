n = int(input('Enter number'))
count = 0
for i in range (0, n + 1):
    for j in range(0, i):
        print('*', end = '')
        count += 1
    print('\n')
print("Number of stars:", count)
