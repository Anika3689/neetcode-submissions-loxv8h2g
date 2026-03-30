class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        windowLetters = set()
        windowLetters.add(s[0])
        maxFoundLen = 1
        left = 0
        for right in range(1, len(s)):
            newLetter = s[right]
            if newLetter in windowLetters:
                while left < right and s[left] != newLetter:
                    windowLetters.remove(s[left])
                    left += 1
                windowLetters.remove(s[left])
                left += 1
            
            windowLetters.add(newLetter)
            maxFoundLen = max(maxFoundLen, right-left+1)
        
        return maxFoundLen