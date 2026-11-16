class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
            
        dpRobLast = [0 for _ in range(n + 2)]
        dpRobLast[n-1] = nums[n-1]
        dpSkipLast = [0 for _ in range(n + 2)]

        for i in range(n-1, -1, -1):
            if i == 0:
                dpRobLast[i] = dpRobLast[i + 1]
            else:
                dpRobLast[i] = max(nums[i] + dpRobLast[i + 2], dpRobLast[i + 1])
            
            if i == n-1:
                dpSkipLast[i] = 0
            else:
                dpSkipLast[i] = max(nums[i] + dpSkipLast[i + 2], dpSkipLast[i + 1])

        return max(dpRobLast[0], dpSkipLast[0])