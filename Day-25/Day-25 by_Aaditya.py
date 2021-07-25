#day25_challenge

class Solution(object):
    def twoSum(self, num, target):
        required = {}
        for i in range(len(num)):
            if target - num[i] in required:
                return [required[target - num[i]],i]
            else:
                required[num[i]]=i

input_list = [4,14,21,1]
ob = Solution()
print(ob.twoSum(input_list, 35))
