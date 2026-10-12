class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        curCounts = {s[0] : 1}
        maxLen = 1
        l = 0 
        for r in range(1, len(s)):
            curCounts[s[r]] = curCounts.get(s[r], 0) + 1
            while curCounts[s[r]] > 1:
                curCounts[s[l]] -= 1
                if curCounts[s[l]] == 0:
                    curCounts.pop(s[l])
                l += 1

            maxLen = max(maxLen, r - l + 1)
        
        return maxLen