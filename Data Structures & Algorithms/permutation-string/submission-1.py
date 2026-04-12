class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Counts = Counter(s1)
        windowCounts = defaultdict(int)
        for i in range(len(s1)):
            windowCounts[s2[i]] += 1

        if s1Counts == windowCounts:
            return True
        
        for r in range(len(s1), len(s2)):
            addChar = s2[r]
            removeChar = s2[r - len(s1)]
            
            windowCounts[addChar] += 1
            if windowCounts[removeChar] <= 1:
                windowCounts.pop(removeChar)
            else:
                windowCounts[removeChar] -= 1

            if windowCounts == s1Counts:
                return True
        
        return False



        

