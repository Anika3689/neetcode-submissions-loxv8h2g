class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacificRes = [[0 for _ in range(n)] for _ in range(m)]
        atlanticRes = [[0 for _ in range(n)] for _ in range(m)]
        queue = deque()

        for j in range(n):
            pacificRes[0][j] = 1
            atlanticRes[m-1][j] = 1
            queue.append((0, j, 'p'))
            queue.append((m-1, j, 'a'))

        for i in range(m):
            pacificRes[i][0] = 1
            atlanticRes[i][n-1] = 1
            queue.append((i, 0, 'p'))
            queue.append((i, n-1, 'a'))

        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        while queue:
            i, j, side = queue.popleft()
            for direction in dirs:
                dy, dx = direction
                if not (0 <= i + dy < m and 0 <= j + dx < n):
                    continue
                if heights[i + dy][j + dx] < heights[i][j]:
                    continue

                if side == 'p' and pacificRes[i + dy][j + dx] != 1:
                    pacificRes[i + dy][j + dx] = 1
                    queue.append((i + dy, j + dx, side))
                if side == 'a' and atlanticRes[i + dy][j + dx] != 1:
                    atlanticRes[i + dy][j + dx] = 1
                    queue.append((i + dy, j + dx, side))
                
        res = []
        for i in range(m):
            for j in range(n):
                if atlanticRes[i][j] and pacificRes[i][j]:
                    res.append([i, j])
        
        return res
