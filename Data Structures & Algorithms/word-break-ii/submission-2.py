class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        # def partition(l):
        #     if l >= len(s):
        #         return ['']

        #     sentences = []
        #     for i in range(l, len(s)):
        #         curWord = s[l : i + 1]
        #         if curWord not in wordDict:
        #             continue

        #         subs = partition(i + 1)
        #         for sub in subs:
        #             if not sub:
        #                 sentences.append(curWord)
        #             else:
        #                 sentences.append(curWord + ' ' + sub)
                
        #     return sentences

        dp = [[] for _ in range(len(s) + 1)]
        dp[-1].append('')
        for l in range(len(s) - 1, -1, -1):
            for r in range(l + 1, len(s) + 1):
                curWord = s[l : r]
                if curWord not in wordDict:
                    continue
                for sub in dp[r]:
                    if not sub:
                        dp[l].append(curWord)
                    else:
                        dp[l].append(curWord + ' ' + sub)
        
        return dp[0]



                




        