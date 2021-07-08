n = int(input(" Enter n : "))
m = int(input(" Enter m : "))
sum = 0

for num in range(n, m+1):
    if(num % 2 == 0):
        sum = sum + num

print("The Sum of Even Numbers from "+str(n)+" to "+str(num)+" = "+str(sum))
