class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])

        u = 0
        b = m - 1
        l = 0
        r = n - 1

        while u <= b and l <= r:
            for j in range(l, r+1):
                res.append(matrix[u][j])
            u += 1
            for i in range(u, b+1):
                res.append(matrix[i][r])
            r -= 1
            if u <= b:
                for j in range(r, l-1, -1):
                    res.append(matrix[b][j])
                b -= 1
            if l <= r:
                for i in range(b, u-1, -1):
                    res.append(matrix[i][l])
                l += 1

        return res
            