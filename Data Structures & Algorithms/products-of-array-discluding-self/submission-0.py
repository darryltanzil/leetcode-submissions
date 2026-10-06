class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res


        # prefix = [1] * (len(nums)+1)
        # for i in range(1,len(nums)+1):
        #     prefix[i] = prefix[i-1] * nums[i-1]
        
        # suffix = [1] * (len(nums)+1)
        # for i in range(len(nums)-2, -1, -1):
        #     suffix[i] = suffix[i+1] * nums[i+1]
        
        # output = [0] * len(nums)
        # for i in range(len(nums)):
        #     output[i] = prefix[i] * suffix[i]
        # return output