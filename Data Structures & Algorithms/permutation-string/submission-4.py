class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1Counts = Counter(s1)
        s2Counts = Counter(s2[:len(s1)])

        for l in range(len(s2) - len(s1) + 1):
            if s1Counts == s2Counts:
                return True

            s2Counts[s2[l]] -= 1
            if s2Counts[s2[l]] == 0:
                s2Counts.pop(s2[l])
            
            r = l + len(s1)
            if r >= len(s2):
                break
            s2Counts[s2[r]] += 1 
        
        return False