n = int(input('Enter number of elements: '))
arr = []

for i in range (0, n):
    x = int(input('Enter element: '))
    arr.append(x)

def maxSubArraySum(a, size):
    max_so_far = a[0]
    curr_max = a[0]
    
    for i in range(1, size):
    	curr_max = max(a[i], curr_max + a[i])
    	max_so_far = max(max_so_far, curr_max)
    return max_so_far

print("Maximum contiguous sum is", maxSubArraySum(arr, len(arr)))
