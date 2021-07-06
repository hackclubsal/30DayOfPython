#Day-6_Hackclubsal_30DayOfPython_Solution
#Program to find ASCII code of the given input Character 
#Convert ASCII Value in to binary

char = input("Enter Character :\n")
print("ASCII Value Of '" + char + "' is :",ord(char))

binary = "{0:b}".format(ord(char))
print("Binary Value is :",binary)

'''
Output :

Enter Character : D
ASCII Value Of 'D' is : 68
Binary Value is : 1000100

Enter Character : d
ASCII Value Of 'd' is : 100
Binary Value is : 1100100

'''
