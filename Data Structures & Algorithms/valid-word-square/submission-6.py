class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        for rowIdx in range(n):
            for colIdx in range(len(words[rowIdx])):
                if colIdx >= n or len(words[colIdx]) <= rowIdx:
                    return False
                
                if words[rowIdx][colIdx] != words[colIdx][rowIdx]:
                    return False

        return True