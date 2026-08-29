class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        
        return len(nums)

        # l = 0
        # r = len(nums) - 1

        # while l <= r:
        #     midpt = (l + r) // 2

