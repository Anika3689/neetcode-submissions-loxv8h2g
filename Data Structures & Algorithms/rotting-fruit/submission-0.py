class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        minMinutes = 0
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        while queue:
            i, j, minute = queue.popleft()
            for direction in dirs:
                dy, dx = direction
                if not (0 <= i + dy < m and 0 <= j + dx < n):
                    continue

                if grid[i + dy][j + dx] == 1:
                    grid[i + dy][j + dx] = 2
                    minMinutes = max(minMinutes, minute + 1)
                    queue.append((i + dy, j + dx, minute + 1))
        
        for row in grid:
            for orange in row:
                if orange == 1:
                    return -1
        
        return minMinutes

            
