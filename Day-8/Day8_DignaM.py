#Day-8_Hackclubsal_30DayOfPython_Solution
#Program to print the sum of all the even numbers between n and m 

start = int(input("Enter the start of range : \n"))
end = int(input("Enter the end of range : \n"))

total = 0

for num in range(start+1, end):
    if(num % 2 == 0):
        total = total + num

print("Sum :",total)

'''
Output

Enter the start of range : 0
Enter the end of range : 10
Sum : 20

Enter the start of range : 4
Enter the end of range : 12
Sum : 24

'''