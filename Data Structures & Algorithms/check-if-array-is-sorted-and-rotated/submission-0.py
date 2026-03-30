class Solution:
    def check(self, nums: List[int]) -> bool:
        numPivots = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                numPivots += 1
            
        if numPivots == 0:
            return True
        if numPivots == 1 and nums[-1] <= nums[0]:
            return True
        return False