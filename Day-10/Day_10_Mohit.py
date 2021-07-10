#sum of the n natural numbers
i =int(input("Enter the number : "))

sum = 0
for i in range(0,int(i)+1):
    sum = sum+i
    
print(sum," is the sum of ",i," numbers.")
