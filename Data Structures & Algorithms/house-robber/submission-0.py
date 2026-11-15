class Solution:
    def rob(self, nums: list[int], i: int = 0) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + 2)]
        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])

        return dp[0]

        # if i >= len(nums):
        #     return 0

        # robHouse = nums[i] + self.rob(nums, i + 2)
        # skipHouse = self.rob(nums, i + 1)

        # return max(robHouse, skipHouse)