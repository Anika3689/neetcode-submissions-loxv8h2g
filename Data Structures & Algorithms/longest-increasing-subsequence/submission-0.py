class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]

        for i in range(1, n):
            longestValidLen = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    longestValidLen = max(longestValidLen, dp[j])
            
            dp[i] += longestValidLen
            
        return max(dp)