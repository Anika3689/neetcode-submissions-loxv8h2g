class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        sideLen = total // 4
        sides = [0 for _ in range(4)]

        if max(matchsticks) > sideLen:
            return False

        def groupSticks(stickIdx):
            if stickIdx >= len(matchsticks):
                return all(totalLen == sideLen for totalLen in sides)

            stickLen = matchsticks[stickIdx]

            for i in range(len(sides)):
                if stickLen + sides[i] > sideLen:
                    continue

                sides[i] += stickLen
                if groupSticks(stickIdx + 1):
                    return True
                sides[i] -= stickLen
            
            return False
        
        return groupSticks(0)



            





