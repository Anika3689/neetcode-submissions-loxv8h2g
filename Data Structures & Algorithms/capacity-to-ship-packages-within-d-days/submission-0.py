class Solution:
    def canShip(self, dailyCap, maxDays, weights) -> bool:
        numUsedDays = 1
        curUsedWeight = 0
        for weight in weights:
            if curUsedWeight + weight > dailyCap:
                curUsedWeight = weight
                numUsedDays += 1
            else:
                curUsedWeight += weight
        
        return numUsedDays <= maxDays

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minWeightCap = max(weights)
        maxWeightCap = sum(weights)
        lowestPossibleCap = maxWeightCap

        while minWeightCap <= maxWeightCap:
            mid = (minWeightCap + maxWeightCap) // 2
            if self.canShip(mid, days, weights):
                lowestPossibleCap = mid
                maxWeightCap = mid - 1
            else:
                minWeightCap = mid + 1

        return lowestPossibleCap
