
def maxSubArraySum(arr,n):
     
    max_so_far =arr[0]
    curr_max = arr[0]
     
    for i in range(1,n):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far
 

n =  int(input("Enter size of array : "))
arr = []
for i in range (0,n) :
    ele = int(input())
    arr.append(ele)
print("Maximum  sum is" , maxSubArraySum(arr,len(arr)))