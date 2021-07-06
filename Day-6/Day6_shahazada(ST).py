charInput=input() #input from user
asciiOfChar=ord(charInput) #convert char to ascii value

print(asciiOfChar)  #output  ascii of char 

print('0'+str(ord(charInput))) #output ascii with leading 0

print(bin(asciiOfChar)) #binary of number by inbuilt function

#creat  a list named binary and store the calculated binary throuh while loop
binary=[]

while(asciiOfChar): #loop runs until asciiOfChar>0
    binary.append(asciiOfChar%2) #append the remainder to the list which form binary digit
    asciiOfChar//=2  # by this (/) division method it give quotient  become floating point that's apply interger division (//)
    
print(''.join([str(i) for i in binary[::-1]]) )   #here i applied list comprehension with reverse list ([: : -1] for reverse the list) and ''.join() fro output like 123 instead 1,2,3 