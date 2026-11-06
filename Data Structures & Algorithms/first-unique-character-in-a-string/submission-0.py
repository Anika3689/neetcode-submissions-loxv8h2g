class Solution:
    def firstUniqChar(self, s: str) -> int:
        # stores {char : [first index, count]}
        charInfo = {} 
        for i in range(len(s)):
            if s[i] in charInfo:
                charInfo[s[i]][1] += 1
            else:
                charInfo[s[i]] = [i, 1]
        
        firstSeenIndex = len(s)
        for char in charInfo:
            index, count = charInfo[char]
            if count > 1:
                continue
            firstSeenIndex = min(firstSeenIndex, index)
        
        return -1 if firstSeenIndex == len(s) else firstSeenIndex
