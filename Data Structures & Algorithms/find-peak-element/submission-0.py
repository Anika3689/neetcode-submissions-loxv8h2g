class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid+1] > nums[mid]:
                l = mid + 1
            else:
                r = mid
        
        return l