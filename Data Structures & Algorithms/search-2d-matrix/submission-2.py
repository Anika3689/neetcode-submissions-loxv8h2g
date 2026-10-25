class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low = 0
        high = m * n - 1

        while low <= high:
            mid = (low + high) // 2
            y = mid // n
            x = mid % n

            if matrix[y][x] == target:
                return True
            elif matrix[y][x] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False