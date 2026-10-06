class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for v in numSet:
            streak = 0
            if v-1 not in numSet: # if this is the start of seq
                while v+streak in numSet:
                    streak += 1
                res = max(res, streak)
        return res