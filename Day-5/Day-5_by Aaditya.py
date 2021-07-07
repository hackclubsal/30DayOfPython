#day5_challenge

month = int(input("Enter the month number: "))
if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
	print("Number of days is 31")
elif(month == 2):
	print(" Number of days is 28")
else:
	print("Number of days is 30")
