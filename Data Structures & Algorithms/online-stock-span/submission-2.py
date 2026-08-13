class StockSpanner:

    def __init__(self):
        self.stack = []
        self.i = 0 # index of next day

    def next(self, price: int) -> int:
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        
        if self.stack:
            _, j = self.stack[-1]
            curSpan = self.i - j
        else:
            curSpan = self.i + 1
        
        self.stack.append((price, self.i))
        self.i += 1
        return curSpan
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)