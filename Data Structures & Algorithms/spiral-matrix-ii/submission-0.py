class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # border indexes of matrix
        u_r = l_c = 0
        b_r = r_c = n - 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        count = 1

        while u_r <= b_r and l_c <= r_c:
            for c in range(l_c, r_c):
                matrix[u_r][c] = count
                count += 1
            if u_r == b_r:
                matrix[u_r][r_c] = count
                break

            for r in range(u_r, b_r):
                matrix[r][r_c] = count
                count += 1
            for c in range(r_c, l_c, -1):
                matrix[b_r][c] = count
                count += 1
            if l_c == r_c:
                matrix[b_r][l_c] = count
                break

            for r in range(b_r, u_r, -1):
                matrix[r][l_c] = count
                count += 1
                
            u_r += 1
            b_r -= 1
            l_c += 1
            r_c -= 1
        
        return matrix
