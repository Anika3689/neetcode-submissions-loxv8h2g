class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        numContentChildren = 0
        cookieIdx = 0
        for childIdx in range(len(g)):
            greedFactor = g[childIdx]
            while cookieIdx < len(s) and s[cookieIdx] < greedFactor:
                cookieIdx += 1

            if cookieIdx >= len(s):
                return numContentChildren
            
            numContentChildren += 1
            cookieIdx += 1
        
        return numContentChildren
