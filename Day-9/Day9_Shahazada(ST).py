#by treating as string and useing inbuilt function
'''
num=input('Enter a number:- ')#take input as a string

lengthOfNumber=len(num)

print(num[lengthOfNumber-1])

if(lengthOfNumber%2):
    print(num[lengthOfNumber//2]) #we use integer because index of string must be integer number not float
'''

#Now as a integer

num=int(input('Enter a number:- '))

temp=num
listOfDigit=[]
while(temp):
    
    if(temp==num):
        lastDigit=temp%10
    
    listOfDigit.append(temp%10)
    temp//=10  
    
print(lastDigit)    

digitLength=len(listOfDigit)
if(digitLength%2):
    print(listOfDigit[digitLength//2]) #we use integer because index of list must be integer number not float
