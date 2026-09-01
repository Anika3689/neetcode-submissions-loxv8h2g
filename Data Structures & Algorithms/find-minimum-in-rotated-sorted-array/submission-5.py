class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums has been sorted n times (effectively not rotated)
        if nums[0] < nums[-1]:
            return nums[0]
        
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            if mid < len(nums)-1 and nums[mid+1] < nums[mid]:
                return nums[mid+1]
            
            if nums[l] > nums[mid]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]
