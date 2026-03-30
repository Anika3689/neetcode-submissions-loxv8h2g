class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nextEmptyIdx = 0
        while nextEmptyIdx < len(nums) and nums[nextEmptyIdx] != 0:
            nextEmptyIdx += 1
        
        for i in range(nextEmptyIdx + 1, len(nums)):
            if nums[i] != 0:
                nums[nextEmptyIdx] = nums[i]
                nums[i] = 0
                nextEmptyIdx += 1
        



