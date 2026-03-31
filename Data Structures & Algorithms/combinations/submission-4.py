class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def enumerateK(curCombo: list, start: int, i: int):
            nonlocal combinations, end
            if i > k:
                combinations.append(curCombo.copy())
                return

            for choice in range(start, end + 1):
                curCombo.append(choice)
                enumerateK(curCombo, choice + 1, i + 1)
                curCombo.pop()


        combinations = []
        start, end = 1, n
        curCombo = []
        enumerateK(curCombo, start, 1)
        return combinations
        
        
