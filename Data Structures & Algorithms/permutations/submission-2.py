class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def helper(curPerm: list, indices: set):
            nonlocal res
            if len(indices) == 0:
                res.append(curPerm.copy())
                return

            for i in indices:
                curPerm.append(nums[i])
                helper(curPerm, indices - {i})
                curPerm.pop()

        indices = {i for i in range(n)}
        helper([], indices)
        return res