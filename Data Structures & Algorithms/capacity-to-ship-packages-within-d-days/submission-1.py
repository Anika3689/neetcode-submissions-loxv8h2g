class Solution:
    def isCapacityValid(self, maxCap, weights, dayLimit):
        days = 1
        curDayTotal = 0
        for weight in weights:
            if weight + curDayTotal > maxCap:
                curDayTotal = weight
                days += 1
            else:
                curDayTotal += weight
        
        return days <= dayLimit

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days == 1:
            return sum(weights)

        low = max(weights)
        high = sum(weights)
        bestWeightCap = high
        
        while low <= high:
            mid = (low + high) // 2
            if self.isCapacityValid(mid, weights, days):
                bestWeightCap = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return bestWeightCap


