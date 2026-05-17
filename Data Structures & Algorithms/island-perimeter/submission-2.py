class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i, j, grid):
            n = len(grid)
            m = len(grid[0])

            if i >= n or j >= m or i < 0 or j < 0:
                return 1
            if grid[i][j] == -1 or grid[i][j] == 0:
                return 0
            
            waterSides = 0
            grid[i][j] = -1
            if j - 1 >= 0 and grid[i][j - 1] == 0:
                waterSides += 1
            if j + 1 < m and grid[i][j + 1] == 0:
                waterSides += 1
            if i + 1 < n and grid[i + 1][j] == 0:
                waterSides += 1
            if i - 1 >= 0 and grid[i - 1][j] == 0:
                waterSides += 1
            
            waterSides += dfs(i, j - 1, grid)
            waterSides += dfs(i, j + 1, grid)
            waterSides += dfs(i + 1, j, grid)
            waterSides += dfs(i - 1, j, grid)

            return waterSides

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j, grid)
                    

        




