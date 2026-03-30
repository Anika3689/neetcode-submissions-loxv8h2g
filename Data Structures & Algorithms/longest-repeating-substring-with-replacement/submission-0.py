class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 1
        frequencies = {}
        frequencies[s[0]] = 1
        mostFreqLetter = s[0]

        left = 0
        for right in range(1, len(s)):
            curLetter = s[right]
            frequencies[curLetter] = frequencies.get(curLetter, 0) + 1

            # If curLetter becomes the new most frequent letter in window
            if frequencies.get(curLetter, 0) > frequencies.get(mostFreqLetter, 0):
                mostFreqLetter = curLetter
            
            windowSize = right - left + 1
            k_leftover = k - (windowSize - frequencies[mostFreqLetter])
            # Slide window up if no more letters can be replaced
            if k_leftover < 0:
                frequencies[s[left]] -= 1
                left += 1
                
            windowSize = right - left + 1
            maxLen = max(maxLen, windowSize)

        return maxLen
