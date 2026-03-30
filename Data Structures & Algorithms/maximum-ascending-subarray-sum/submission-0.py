class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                curSum = 0

            curSum += nums[i]
            maxSum = max(maxSum, curSum)
        
        return maxSum

           