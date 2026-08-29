class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m * n - 1

        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False

        while low <= high:
            midpt = (low + high) // 2 
            rowMid = midpt // n
            colMid = midpt % n
            if matrix[rowMid][colMid] == target:
                return True
            elif matrix[rowMid][colMid] < target:
                low = midpt + 1
            else:
                high = midpt - 1
        
        return False