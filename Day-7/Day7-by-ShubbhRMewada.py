s=''
for i in range(int(input("Enter the value of M: "))+1,int(input("Enter the value of N: "))):
    s+=str(i)+','
print(s.rstrip(','))
