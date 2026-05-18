class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j, grid):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] == -1 or grid[i][j] == '0':
                return

            grid[i][j] = -1
            dfs(i - 1, j, grid)
            dfs(i + 1, j, grid)
            dfs(i, j + 1, grid)
            dfs(i, j - 1, grid)
        
        numIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(row, col, grid)
                    numIslands += 1 
                    
        return numIslands
            