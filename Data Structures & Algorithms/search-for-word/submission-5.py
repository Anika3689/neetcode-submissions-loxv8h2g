class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def check(i, j, wordIndex, visited):
            if wordIndex >= len(word):
                return True
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return False

            if (i, j) in visited:
                return False
            visited.add((i, j))

            if board[i][j] != word[wordIndex]:
                visited.remove((i, j))
                return False
            
            wordIndex += 1
            lCheck, rCheck, upCheck, downCheck = 0,0,0,0
            if j >= 0:
                lCheck = check(i, j - 1, wordIndex, visited)
            if j <= len(board[0]) - 1:
                rCheck = check(i, j + 1, wordIndex, visited)     
            if i >= 0:
                upCheck = check(i - 1, j, wordIndex, visited)
            if i <= len(board) - 1:
                downCheck = check(i + 1, j, wordIndex, visited)
            
            visited.remove((i, j))
            return lCheck or rCheck or upCheck or downCheck


        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and check(i, j, 0, visited):
                    return True
        return False


    # A B C E
    # S F C S
    # A D E E
 
 # ABCB
