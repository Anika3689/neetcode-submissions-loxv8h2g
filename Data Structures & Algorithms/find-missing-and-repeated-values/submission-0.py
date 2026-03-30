class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = [0 for _ in range(n * n)]
        ans = [0] * 2

        for row in grid:
            for elem in row:
                if seen[elem - 1]:
                    ans[0] = elem
                else:
                    seen[elem - 1] = 1
        
        for i in range(len(seen)):
            if not seen[i]:
                ans[1] = i + 1
        
        return ans
        


