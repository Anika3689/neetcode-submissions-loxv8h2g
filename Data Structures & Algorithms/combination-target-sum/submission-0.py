class Solution:
    # All numbers are positive -> once curSum exceeds target, return from current path

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def generate(i, curList, curSum):
            nonlocal res
            if curSum == target:
                res.append(curList.copy())
            
            if curSum >= target or i >= len(nums):
                return
            
            generate(i+1, curList, curSum)
            curList.append(nums[i])
            generate(i, curList, curSum + nums[i])
            curList.pop()
        
        generate(0, [], 0)
        return res
