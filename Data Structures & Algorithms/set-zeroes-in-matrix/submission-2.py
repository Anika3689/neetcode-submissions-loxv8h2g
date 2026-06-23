class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        firstColZero = False
        firstRowZero = False

        for r in range(m):
            for c in range(n):
                if matrix[r][c] != 0:
                    continue
                if c == 0:
                    firstColZero = True
                if r == 0:
                    firstRowZero = True
                matrix[0][c] = 0
                matrix[r][0] = 0
        
        for r in range(1, m):
            if matrix[r][0] == 0:
                for c in range(1, n):
                    matrix[r][c] = 0
        
        for c in range(1, n):
            if matrix[0][c] == 0:
                for r in range(1, m):
                    matrix[r][c] = 0
        
        if firstColZero:
            for r in range(m):
                matrix[r][0] = 0
        if firstRowZero:
            for c in range(n):
                matrix[0][c] = 0
