class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        span = 1
        if not self.stk:
            self.stk.append((price, span))
            return span
        
        totalDays = len(self.stk)
        i = totalDays - 1
        while i >= 0:
            past_price, past_span = self.stk[i]
            if past_price > price:
                break
            i -= past_span

        span = totalDays - i
        self.stk.append((price, span))
        return span
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)