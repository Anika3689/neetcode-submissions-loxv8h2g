class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        allSubs = []
        def getSubsets(curSubset: list, index: int):
            if index >= len(nums):
                allSubs.append(curSubset.copy())
                return
            
            curSubset.append(nums[index])
            getSubsets(curSubset, index + 1)
            curSubset.pop()
            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1
            getSubsets(curSubset, index + 1)


        subset = []
        nums.sort()
        getSubsets(subset, 0)
        return allSubs