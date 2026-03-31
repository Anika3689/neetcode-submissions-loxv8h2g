class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def enumerateK(curCombo: list, start: int, used: set, i: int):
            nonlocal combinations, end
            if i > k:
                combinations.append(curCombo.copy())
                return

            for choice in range(start, end + 1):
                if choice in used:
                    continue
                used.add(choice)
                curCombo.append(choice)
                enumerateK(curCombo, choice + 1, used, i + 1)
                used.remove(choice)
                curCombo.pop()


        combinations = []
        start, end = 1, n
        used = set()
        curCombo = []
        enumerateK(curCombo, start, used, 1)
        return combinations
        
        
