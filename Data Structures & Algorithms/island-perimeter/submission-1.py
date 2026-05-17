class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i, j, grid, visited):
            n = len(grid)
            m = len(grid[0])

            if i >= n or j >= m or i < 0 or j < 0:
                return 1
            if visited[i][j] or (grid[i][j] == 0):
                return 0
            
            waterSides = 0
            visited[i][j] = 1
            if j - 1 >= 0 and grid[i][j - 1] == 0:
                waterSides += 1
            if j + 1 < m and grid[i][j + 1] == 0:
                waterSides += 1
            if i + 1 < n and grid[i + 1][j] == 0:
                waterSides += 1
            if i - 1 >= 0 and grid[i - 1][j] == 0:
                waterSides += 1
            
            waterSides += dfs(i, j - 1, grid, visited)
            waterSides += dfs(i, j + 1, grid, visited)
            waterSides += dfs(i + 1, j, grid, visited)
            waterSides += dfs(i - 1, j, grid, visited)

            return waterSides


        visited = [[0 for _ in grid[0]] for _ in grid]
        startLandCell = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    startLandCell = (i, j)
                    break

        return dfs(*startLandCell, grid, visited)




