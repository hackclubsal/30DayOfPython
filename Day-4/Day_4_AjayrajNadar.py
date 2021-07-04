n = int(input("Enter a number:-"))

myList = []

for i in range(1,n+1):
    myList.append("*"*i)
print("\n".join(myList))
 
count = (n*(n+1))/2
print("Total stars : ",int(count))