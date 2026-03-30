class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)
        letterIndices = defaultdict(list)
        for i in range(n):
            letterIndices[s[i]].append(i)

        for curShift in shift:
            direction, amount = curShift

            for ch in letterIndices:
                for i in range(len(letterIndices[ch])):
                    # Shift left
                    if direction == 0:
                        letterIndices[ch][i] = (letterIndices[ch][i] - amount) % n
                    else:
                    # Shift right
                        letterIndices[ch][i] = (letterIndices[ch][i] + amount) % n
    
        
        res = [None for _ in range(n)]
        for letter in letterIndices:
            for index in letterIndices[letter]:
                res[index] = letter
        
        return ''.join(res)





