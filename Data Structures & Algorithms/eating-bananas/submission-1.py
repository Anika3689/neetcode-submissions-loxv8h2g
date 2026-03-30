class Solution:

    def isBananaRatePossible(self, piles, k, h):
        hoursTaken = 0
        for pile in piles:
            hoursTaken += math.ceil(pile / k)
        return hoursTaken <= h
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = 1
        maxK = max(piles)
        bestValidK = maxK

        while minK <= maxK:
            mid = (maxK + minK) // 2
            kPossible = self.isBananaRatePossible(piles, mid, h)
            if kPossible:
                bestValidK = mid
                maxK = mid - 1
            else:
                minK = mid + 1
        
        return bestValidK