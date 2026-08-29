class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            midpt = (l + r) // 2
            if nums[midpt] == target:
                return midpt
            elif nums[midpt] < target:
                l = midpt + 1
            else:
                r = midpt - 1

        return l


