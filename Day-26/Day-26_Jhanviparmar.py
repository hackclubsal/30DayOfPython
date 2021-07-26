#day26
nums=[-2,1,-3,4,-1,2,1,-5,4]
result = [nums.pop(0)]
for i in range(len(nums)):
    result.append(max (nums[i] , result[-1] + nums[i]))
print(max(result))
