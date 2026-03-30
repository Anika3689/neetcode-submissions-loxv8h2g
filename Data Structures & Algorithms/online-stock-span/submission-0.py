class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        self.stk.append(price)
        totalDays = len(self.stk)
        i = totalDays - 1
        while i >= 0 and self.stk[i] <= price:
            i -= 1
        return totalDays - (i+1)
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)