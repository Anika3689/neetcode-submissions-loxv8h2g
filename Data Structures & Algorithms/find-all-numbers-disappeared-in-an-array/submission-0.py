class Solution:
    # [4,-3,-2,-7,8,2,-3,-1]
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            val = abs(num)
            if nums[val - 1] > 0:
                nums[val - 1] *= -1

        res = []
        for i in range(len(nums)):
            val = nums[i]
            if val > 0:
                res.append(i + 1)
        
        return res
        
