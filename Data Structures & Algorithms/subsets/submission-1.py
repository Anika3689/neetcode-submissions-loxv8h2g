class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubs = []
        def getSubsets(curSub: list, idx: int):
            if idx >= len(nums):
                allSubs.append(curSub)
                return
            
            getSubsets(curSub + [nums[idx]], idx + 1)
            getSubsets(curSub, idx + 1)
        
        curSub = []
        getSubsets(curSub, 0)
        return allSubs

            
