class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def generate(i, curList):
            nonlocal res
            if i >= len(nums):
                res.append(curList)
                return
            
            generate(i + 1, curList + [nums[i]])
            generate(i + 1, curList)
        
        generate(0, [])
        return res
