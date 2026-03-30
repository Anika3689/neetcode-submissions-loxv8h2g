class Solution:
    # 6,11
    # 8
    # Position of midpt:
    # 8/4, 8%4 -> matrix[2][0]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nRows, nCols = len(matrix), len(matrix[0])
        low = 0
        high = nRows * nCols - 1

        while low <= high:
            mid = (low + high) // 2
            # Get the actual position of midpoint from its flattened index
            midPos = mid // nCols, mid % nCols
            midVal = matrix[midPos[0]][midPos[1]]
            if midVal == target:
                return True
            elif midVal < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False