class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestRepLen = 0
        freq = {}
        maxCharFreq = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxCharFreq = max(maxCharFreq, freq[s[r]])

            while (r - l + 1) - maxCharFreq > k:
                freq[s[l]] -= 1
                l += 1
            
            longestRepLen = max(longestRepLen, r - l + 1)
        
        return longestRepLen



