class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len, s2Len = len(s1), len(s2)
        if s1Len > s2Len:
            return False
        
        s1charFreqs = Counter(s1)
        s2charFreqs = Counter(s2[:s1Len])
        if s1charFreqs == s2charFreqs:
            return True

        for start in range(1, s2Len - s1Len + 1):
            s2charFreqs[s2[start-1]] -= 1
            end = start + s1Len - 1
            s2charFreqs[s2[end]] = s2charFreqs.get(s2[end], 0) + 1
            if s1charFreqs == s2charFreqs:
                return True
        
        return False