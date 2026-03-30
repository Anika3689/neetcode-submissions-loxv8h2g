class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPriceSeen = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            curProfit = prices[i] - minPriceSeen
            maxProfit = max(maxProfit, curProfit)
            minPriceSeen = min(minPriceSeen, prices[i])

        return maxProfit