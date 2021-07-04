x= int(input('Enter number of rows'))     
count = 0                                 
for i in range (0, x + 1):                
    for j in range(0, i):                 
        print('*', end = '')              
        count = count+ 1                  
    print('\n')                           
print("Number of stars:", count)          
