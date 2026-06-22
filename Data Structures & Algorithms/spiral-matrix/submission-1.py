class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        # border indexes of matrix
        u_r = 0
        b_r = m - 1
        l_c = 0
        r_c = n - 1

        res = []
        while u_r <= b_r and l_c <= r_c:
            for c in range(l_c, r_c):
                res.append(matrix[u_r][c])
            if u_r == b_r:
                res.append(matrix[u_r][r_c])
                break

            for r in range(u_r, b_r):
                res.append(matrix[r][r_c])
            for c in range(r_c, l_c, -1):
                res.append(matrix[b_r][c])
            if l_c == r_c:
                res.append(matrix[b_r][l_c])
                break

            for r in range(b_r, u_r, -1):
                res.append(matrix[r][l_c])
            u_r += 1
            b_r -= 1
            l_c += 1
            r_c -= 1
        
        return res
