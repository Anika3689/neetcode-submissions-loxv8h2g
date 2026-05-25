class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        borderOs = set()
        for i in range(m):
            if board[i][0] == 'O':
                borderOs.add((i, 0))
            if board[i][n-1] == 'O':
                borderOs.add((i, n-1))
        for j in range(n):
            if board[0][j] == 'O':
                borderOs.add((0, j))
            if board[m-1][j] == 'O':
                borderOs.add((m-1, j))
        
        uncapturableSpots = set()
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if (i, j) in uncapturableSpots or board[i][j] == 'X':
                return

            uncapturableSpots.add((i, j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i, j in borderOs:
            dfs(i, j)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O' and (i, j) not in uncapturableSpots:
                    board[i][j] = 'X'
        
        
        



        