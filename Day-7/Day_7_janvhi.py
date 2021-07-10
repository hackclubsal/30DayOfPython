min = int(input("Please Enter the Minimum integer Value : "))
max = int(input("Please Enter the Maximum integer Value : "))

print("The List of Natural Numbers are".format(min, max))

for i in range(min+1, max ):
    print (i, end = '  ')
