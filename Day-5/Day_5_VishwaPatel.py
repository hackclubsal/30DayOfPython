n = int(input(('Enter month')))
dict = {}

for k in range(1, 13):
    dict[k] = ''
    
for k, v in dict.items():
    if ( k <= 7 ):
        if (k % 2 == 0):
            dict[k] = 30
        else:
            dict[k] = 31
    else:
        if (k % 2 == 0):
            dict[k] = 31
        else:
            dict[k] = 30

for keys, values in dict.items():
    if (keys == n ):
        print(dict[keys])
