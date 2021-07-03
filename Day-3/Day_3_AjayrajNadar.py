n=int(input('Enter a Number: '))

if n%10 == 0 and n%20 == 0:
    print("Yes,the number "+str(n)+" is divisible by both 10 and 20")
else:
    print("No,the number "+str(n)+" is not divisible by both 10 and 20")