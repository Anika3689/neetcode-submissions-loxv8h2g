class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        setColumns = [0 for _ in range(n)]
        setNegDiagonals = set()
        setPosDiagonals = set()

        def helper(curGrid, solutions, r):
            if r == n:
                board_rep = [''.join(row) for row in curGrid]
                solutions.append(board_rep)
                return
            
            for c in range(n):
                if setColumns[c]:
                    continue
                if (c - r) in setNegDiagonals:
                    continue
                if (c + r) in setPosDiagonals:
                    continue
                
                curGrid[r][c] = 'Q'
                setColumns[c] = 1
                setNegDiagonals.add(c - r)
                setPosDiagonals.add(c + r)
                
                helper(curGrid, solutions, r + 1)

                curGrid[r][c] = '.'
                setColumns[c] = 0
                setNegDiagonals.remove(c - r)
                setPosDiagonals.remove(c + r)
            
            return 
        
        curGrid = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []
        helper(curGrid, solutions, 0)
        return solutions


