class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums[0] >= target:
            return 1

        n = len(nums)
        windowSum = nums[0]
        minLen = n + 1
        l = 0
        for r in range(1, n):
            windowSum += nums[r]
            while l <= r and windowSum >= target:
                minLen = min(minLen, r - l + 1)
                windowSum -= nums[l]
                l += 1
        
        return minLen if minLen <= n else 0