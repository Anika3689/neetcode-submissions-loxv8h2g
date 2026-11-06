class Solution:
    def maxDepth(self, s: str) -> int:
        numOpen = 0
        res = 0
        for ch in s:
            if ch == '(':
                numOpen += 1
                res = max(res, numOpen)
            elif ch == ')':
                numOpen -= 1
        
        return res
            