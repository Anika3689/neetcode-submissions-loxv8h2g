class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curSum = nums[0]
        maxSum = curSum

        for i in range(1, len(nums)):
            if curSum < 0:
                curSum = 0
            curSum += nums[i]

            maxSum = max(curSum, maxSum)
            
        return maxSum
