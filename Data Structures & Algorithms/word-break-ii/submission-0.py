class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        

        def partition(l):
            if l >= len(s):
                return ['']

            sentences = []
            for i in range(l, len(s)):
                curWord = s[l : i + 1]
                if curWord not in wordDict:
                    continue

                subs = partition(i + 1)
                for sub in subs:
                    if not sub:
                        sentences.append(curWord)
                    else:
                        sentences.append(curWord + ' ' + sub)
                
            return sentences

        sentences = partition(0)
        return sentences