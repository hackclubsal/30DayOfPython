# Day-11_Hackclubsal_30DayOfPython_Solution
# Function to find the nth Fibonacci number
def fib(n):
 
    if n <= 1:
        return n
 
    previousFib = 0
    currentFib = 1
 
    for i in range(n - 1):
        newFib = previousFib + currentFib
        previousFib = currentFib
        currentFib = newFib
 
    return currentFib
 
 
if __name__ == '__main__':
 
    n = int(input("Enter Num : \n"))
    print("Nth Fibonacci number is", fib(n))
    
    
 