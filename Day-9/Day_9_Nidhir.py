n=int(input("Enter n"))
n=abs(n)                #So that it also works with negative number
length=len(str(n))      ##ADVANCE##
for i in range(n+1):
    if i >10 :
        print(n%10)
        break
else:
    print("The Last digit is ",n)


####ADVANCE#####

middle=length%2
if (length)%2 ==0:
        print ("-1 (Its even)")
else:
    print ("The middle digit is ",int(n/(10**(length//2)))%10)