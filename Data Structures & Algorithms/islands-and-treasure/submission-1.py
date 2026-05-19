class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))

        INF = 2147483647
        while queue:
            i, j, dist = queue.popleft()
            if grid[i][j] == INF or grid[i][j] == 0:
                grid[i][j] = dist
            else:
                continue
            
            print(i + 1, j)
            if i + 1 < m and grid[i + 1][j] not in (0, -1):
                queue.append((i + 1, j, dist + 1))
            if i - 1 >= 0 and grid[i - 1][j] not in (0, -1):
                queue.append((i - 1, j, dist + 1))
            if j + 1 < n and grid[i][j + 1] not in (0, -1):
                queue.append((i, j + 1, dist + 1))
            if j - 1 >= 0 and grid[i][j - 1] not in (0, -1):
                queue.append((i, j - 1, dist + 1))




        