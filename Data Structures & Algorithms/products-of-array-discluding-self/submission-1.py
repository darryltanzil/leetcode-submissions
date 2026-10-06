class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        calculate the prefix and postfix product
        can do it as a running sum by keeping a res array, and then
        calculating all the prefix and then calculting the postfix
        """
        res = [1] * len(nums)
        prefix = 1
        for i in range(0, len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res