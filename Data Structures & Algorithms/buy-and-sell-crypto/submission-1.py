class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        futureMaxes = [0 for _ in range(n)]
        futureMaxes[n-1] = prices[n-1]

        for i in range(n-2, -1, -1):
            futureMaxes[i] = max(prices[i], futureMaxes[i+1])
        
        maxProfit = 0
        for i in range(n-1):
            maxProfit = max(maxProfit, futureMaxes[i+1] - prices[i])
        
        return maxProfit