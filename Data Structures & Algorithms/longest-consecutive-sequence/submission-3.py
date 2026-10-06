class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [2,20,4,10,3,4,5]
                 ^

        """
        numSet = set(nums)
        res = 0
        for v in nums:
            currLen = 1
            currV = v
            if v-1 not in numSet:
                while currV+1 in numSet:
                    currLen += 1
                    currV += 1
            res = max(res, currLen)
        return res