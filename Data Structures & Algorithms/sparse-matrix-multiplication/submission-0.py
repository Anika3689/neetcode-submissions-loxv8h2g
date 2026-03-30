class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        mat1Rows = len(mat1)
        mat1Cols = len(mat1[0])
        mat2Cols = len(mat2[0]) 

        res = [[0 for _ in range(mat2Cols)] for _ in range(mat1Rows)]

        for i in range(mat1Rows):
            for j in range(mat2Cols):
                for compIdx in range(mat1Cols):
                    res[i][j] += mat1[i][compIdx] * mat2[compIdx][j]
        
        return res