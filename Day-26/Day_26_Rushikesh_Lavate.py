"""Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum."""
import numpy
def create_array():
    arr = numpy.random.randint(-9,9,numpy.random.randint(5,9))
    return [i for i in arr]

def MaxSum():
    #arr = [-2,1,-3,4,-1,2,1,-5,4]
    arr = create_array()
    print(arr)
    if len(arr)>1:
        maxsum = 0
        cursum = 0
        for i in arr:
            cursum = cursum + i
            if(cursum > maxsum):
                maxsum = cursum
            if cursum < 0:
                cursum = 0
        return maxsum
    else:
        return arr[0]
print('Max sum of subarray is : ',MaxSum())
