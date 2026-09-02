class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        longestPal = (0, 0)
        longestLen = 1

        for i in range(n):
            dp[i][i] = True
            if i < n-1:
                dp[i][i+1] = True if s[i] == s[i+1] else False
                if dp[i][i+1] and 2 > longestLen:
                    longestLen = 2
                    longestPal = (i, i+1)

        for i in range(2, n):
            l = 0
            for r in range(i, n):
                if s[l] != s[r]:
                    dp[l][r] = False

                elif dp[l+1][r-1]:
                    dp[l][r] = True

                if dp[l][r] and r - l + 1 > longestLen:
                    longestLen = r - l + 1
                    longestPal = (l, r)

                l += 1

        return s[longestPal[0]:longestPal[1] + 1]
        