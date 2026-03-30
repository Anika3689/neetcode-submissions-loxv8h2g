class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            midpt = (left + right) // 2
            if nums[midpt] == target:
                return midpt
            if nums[midpt] < target:
                left = midpt + 1
            else:
                right = midpt - 1
        
        return -1