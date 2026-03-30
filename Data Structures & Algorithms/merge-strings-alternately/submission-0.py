class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = [0 for _ in range(len(word1)+len(word2))]
        resIdx = 0
        while i < len(word1) and i < len(word2):
            res[resIdx] = word1[i]
            resIdx += 1
            res[resIdx] = word2[i]
            resIdx += 1
            i += 1
        
        while i < len(word1):
            res[resIdx] = word1[i]
            i += 1
            resIdx += 1
        while i < len(word2):
            res[resIdx] = word2[i]
            i += 1
            resIdx += 1
        
        return ''.join(res)