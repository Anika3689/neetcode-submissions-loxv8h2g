class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        totalSum = 0
        def getSubsets(subsetIndex, curSum):
            nonlocal totalSum
            if subsetIndex >= len(nums):
                totalSum += curSum
                return
            
            # Including cur element in this subset
            getSubsets(subsetIndex + 1, curSum ^ nums[subsetIndex])
            # Excluding
            getSubsets(subsetIndex + 1, curSum)
            
        curSum = 0
        getSubsets(0, curSum)
        return totalSum