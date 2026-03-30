class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        monoInc = True
        monoDec = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                monoDec = False
            elif nums[i] < nums[i - 1]:
                monoInc = False
        
        return monoDec or monoInc