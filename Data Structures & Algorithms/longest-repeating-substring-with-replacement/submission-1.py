class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        charFreqs = {s[0] : 1}
        majorityFreq = s[0]
        bestLen = 1
        l = 0
        
        for r in range(1, n):
            charFreqs[s[r]] = charFreqs.get(s[r], 0) + 1
            majorityLetter = max(charFreqs, key=lambda letter : charFreqs[letter])
            # shrink current window/string until it is valid 
            while l < r and (r - l + 1) - charFreqs[majorityLetter] > k:
                charFreqs[s[l]] -= 1
                majorityLetter = max(charFreqs, key=lambda letter : charFreqs[letter])
                l += 1

            bestLen = max(bestLen, r - l + 1) 
            
        
        return bestLen


