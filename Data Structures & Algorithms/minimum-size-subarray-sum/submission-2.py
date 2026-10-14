class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        minimalLen = len(nums) + 1
        curSum = 0

        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minimalLen = min(minimalLen, r - l + 1)
                curSum -= nums[l]
                l += 1
        
        if minimalLen > len(nums):
            return 0
            
        return minimalLen