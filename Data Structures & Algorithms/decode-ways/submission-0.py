class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n+1)]
        for l in range(n-1, -1, -1):
            if s[l] == '0':
                continue
            for i in range(l + 1, min(n+1, l+3)):
                firstGroup = int(s[l:i])
                if firstGroup > 26:
                    break

                if i >= n:
                    dp[l] += 1
                else:
                    dp[l] += dp[i]

        return dp[0]