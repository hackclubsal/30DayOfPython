#Day-4 Challenge

#-> Question: Write a code for print pyramid and how many stars in it.

#-> Input: Take input from the user and store it in the given variable.
#-> Output: Print a pyramid for given value and stars count.

#-> Example
#Input: 6
#Output:    
#        *
#	     * *
#	     * * *
#	     * * * *
#	     * * * * *
#	     * * * * * *
#        21

n=int(input())

print("-----Method 1 : Explicitly Counting-----")
for i in range(n):
    print("* "*(i+1), end=" ")
    print()
print(f"Number of Stars : {(n*(n+1))//2}")

print("-----Method 2 : Step wise counting-----")
count=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
        count+=1
    print()
print(f"Number of Stars : {count}")
