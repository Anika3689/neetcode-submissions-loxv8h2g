class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [1 for _ in nums]
        rightProducts = [1 for _ in nums]

        for i in range(1, len(nums)):
            leftProducts[i] = leftProducts[i-1] * nums[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            rightProducts[i] = rightProducts[i+1] * nums[i+1]

        result = [leftProducts[i] * rightProducts[i] for i in range(len(nums))]
        return result