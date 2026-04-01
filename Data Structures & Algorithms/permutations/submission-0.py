class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        allPermutations = []

        def helper(curPermutation: list, used: set):
            if len(curPermutation) == len(nums):
                allPermutations.append(curPermutation.copy())
                return
            
            for num in nums:
                if num in used:
                    continue
                curPermutation.append(num)
                used.add(num)
                helper(curPermutation, used)
                curPermutation.pop()
                used.remove(num)
        
        curPermutation = []
        used = set()
        helper(curPermutation, used)
        return allPermutations
            



            
            
