class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [2,20,4,10,3,4,5]
                 ^

        """
        numSet = set(nums)
        res = 0
        for v in nums:
            if v-1 not in numSet:
                currNum = v
                currStreak = 1
                while currNum+1 in numSet:
                    currNum += 1
                    currStreak += 1
                res = max(res, currStreak)
        return res