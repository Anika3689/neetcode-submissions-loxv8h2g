class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums) - 1
        while i >= 0:
            num = nums[i]
            numCount = 0
            while nums[i] == num and i >= 0:
                numCount += 1
                i -= 1
            
            if numCount == 1:
                return num
        
        return -1
            

