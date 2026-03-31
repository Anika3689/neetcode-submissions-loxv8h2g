class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(curCombo: list, curSum: int, index: int):
            if curSum == target:
                uniqueCombos.add(tuple(curCombo))
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
        uniqueCombos = set()
        curCombo = []
        helper(curCombo, 0, 0)
        uniqueCombos = [list(combo) for combo in uniqueCombos]
        return uniqueCombos