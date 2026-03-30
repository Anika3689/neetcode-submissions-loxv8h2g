class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        windowSum = 0
        minLen = float('inf')

        for right in range(n):
            windowSum += nums[right]
            while windowSum >= target:
                minLen = min(minLen, right - left + 1)
                windowSum -= nums[left]
                left += 1

        return 0 if minLen == float('inf') else minLen