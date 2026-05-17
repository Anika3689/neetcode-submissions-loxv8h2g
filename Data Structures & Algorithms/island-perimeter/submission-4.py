class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i, j, grid):
            n = len(grid)
            m = len(grid[0])

            if i >= n or j >= m or i < 0 or j < 0:
                return 1
            if grid[i][j] == 0:
                return 1
            if grid[i][j] == -1:
                return 0

            grid[i][j] = -1
            
            return (
                dfs(i, j - 1, grid) +
                dfs(i, j + 1, grid) +
                dfs(i + 1, j, grid) +
                dfs(i - 1, j, grid)
            )

            return waterSides

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j, grid)
                    

        




