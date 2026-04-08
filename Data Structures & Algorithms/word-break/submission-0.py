class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # def partition(l: int):
        #     if l == len(s):
        #         return True

        #     for r in range(l, len(s)):
        #         if s[l : r + 1] not in words:
        #             continue
        #         if partition(r + 1):
        #             return True
            
        #     return False

        # return partition(0)

        words = set(wordDict)

        dp = [False for _ in range(len(s))]
        if s[-1] in words:
            dp[-1] = True

        for i in range(len(s) - 2, -1, -1):
            for r in range(i, len(s)):
                if s[i : r + 1] in words and (r == len(s) - 1 or dp[r + 1]):
                    dp[i] = True

        return dp[0]


