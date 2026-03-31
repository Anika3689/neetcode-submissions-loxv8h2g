class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(curCombo: list, curSum: int, index: int):
            nonlocal uniqueCombos
            if curSum == target:
                uniqueCombos.append(curCombo.copy())
                return
            if curSum > target or index >= len(candidates):
                return
            
            curNum = candidates[index]
            curCombo.append(curNum)

            helper(curCombo, curSum + curNum, index + 1)
            curCombo.pop()
            while index < len(candidates) and candidates[index] == curNum:
                index += 1
            helper(curCombo, curSum, index)
            
        
        candidates.sort()
        uniqueCombos = []
        curCombo = []
        helper(curCombo, 0, 0)
        return uniqueCombos