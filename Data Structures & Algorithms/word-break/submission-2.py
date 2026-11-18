class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        cached = {}
        
        def canSegment(s, l=0):
            nonlocal cached
            if l in cached:
                return cached[l]

            if l >= len(s):
                return True
            for i in range(l+1, len(s)+1):
                if s[l:i] in words and canSegment(s, i):
                    cached[l] = True
                    return True

            cached[l] = False
            return False

        return canSegment(s)



        # n = len(s)
        # dp = [False for _ in range(n+1)]
        # dp[n] = True

        # for i in range(n-1, -1, -1):
        #     if s[:i+1] in words and dp[i+1]:
        #         return True