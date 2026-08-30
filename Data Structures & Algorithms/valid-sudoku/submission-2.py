class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subboxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == '.':
                    continue
                if val in rows[r] or val in cols[c]:
                    return False
                rows[r].add(val)
                cols[c].add(val)

                boxY = r // 3
                boxX = c // 3

                if val in subboxes[boxY][boxX]:
                    return False
                subboxes[boxY][boxX].add(val)

        return True
                