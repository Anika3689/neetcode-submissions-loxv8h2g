class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestLen = min(len(word) for word in strs)
        i = 0
        while i < shortestLen:
            ch = None
            for word in strs:
                if ch is None or word[i] == ch:
                    ch = word[i]
                else:
                    return word[:i]
            i += 1
        return strs[0][:i]