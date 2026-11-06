class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        #prices = [8, 4, 6, 2, 7, 3, 9, 1, 5, 4]
        # holds an increasing sequence
        stack = [] 
        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                l = stack.pop()
                prices[l] -= prices[i]
            
            stack.append(i)
        
        return prices





