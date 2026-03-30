class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Transform word1 into word2
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[m][n] = 0
        for j in range(n-1, -1, -1):
            dp[m][j] = n - j
        for i in range(m-1, -1, -1):
            dp[i][n] = m - i

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                    continue
                insert_cost = dp[i][j+1]
                replace_cost = dp[i+1][j+1]
                delete_cost = dp[i+1][j]
                dp[i][j] = 1 + min(insert_cost, replace_cost, delete_cost)
        
        return dp[0][0]