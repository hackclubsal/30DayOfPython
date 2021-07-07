# Day-7_Hackclubsal_30DayOfPython_Solution
# Python program to print Numbers in given range 

start = int(input("Enter the start of range:\n")) 
end = int(input("Enter the end of range:\n")) 

for num in range(start+1, end): 
    if num >= 0: 
        print(num, end = " ")
        
'''
Output 

Enter the start of range: 4
Enter the end of range: 12
5 6 7 8 9 10 11 

'''