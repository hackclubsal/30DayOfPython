n = int(input("enter size of array"))
array = []
for i in range(0, n):
    x= int(input("enter element"))
    array.append(x)
target = int(input("Enter target"))

def checksum(array,target):
	for i in range(len(array)):
		for j in range(i+1,len(array)):
			if array[i]+array[j]==target:
				return i,j
	return 0
if checksum(array,target)==0:
	print("Target not found")
else:
	print(checksum(array, target))
