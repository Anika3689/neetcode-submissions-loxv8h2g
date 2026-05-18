class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] == -1 or grid[i][j] == 0:
                return 0

            grid[i][j] = -1
            area1 = dfs(i - 1, j, grid)
            area2 = dfs(i + 1, j, grid)
            area3 = dfs(i, j + 1, grid)
            area4 = dfs(i, j - 1, grid)

            return 1 + area1 + area2 + area3 + area4
        
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    islandArea = dfs(row, col, grid)
                    maxArea = max(maxArea, islandArea)
                    
        return maxArea