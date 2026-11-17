class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str, i=0, j=0) -> int:
        m = len(text1) + 1
        n = len(text2) + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]

        # if i >= len(text1) or j >= len(text2):
        #     return 0
        
        # if text1[i] == text2[j]:
        #     return 1 + self.longestCommonSubsequence(text1, text2, i + 1, j + 1)
        
        # return max(self.longestCommonSubsequence(text1, text2, i + 1, j),
        #             self.longestCommonSubsequence(text1, text2, i, j + 1))