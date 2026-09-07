class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i, visited):
            if r >= len(board) or c >= len(board[0]) or r < 0 or c < 0:
                return i == len(word)
            if i == len(word):
                return True
            if (r, c) in visited or board[r][c] != word[i]:
                return False
            
            visited.add((r, c))
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dy, dx in dirs:
                if dfs(r + dy, c + dx, i + 1, visited):
                    return True
            
            visited.remove((r, c))
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0, set()):
                    return True
        
        return False
            
            
