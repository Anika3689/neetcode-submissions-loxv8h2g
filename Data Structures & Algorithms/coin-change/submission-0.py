class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            minCoins = i + 1
            for denom in coins:
                if denom > i:
                    continue
                remainingCoins = dp[i - denom]
                if remainingCoins != -1:
                    minCoins = min(minCoins, remainingCoins + 1)
            
            dp[i] = minCoins if minCoins <= i else -1
        
        return dp[amount]
