class MedianFinder:

    def __init__(self):
        self.lowerHalf = [] 
        self.upperHalf = []

    def rebalance_halves(self) -> None:
        while len(self.lowerHalf) - len(self.upperHalf) > 1:
            heapq.heappush(self.upperHalf, heapq.heappop_max(self.lowerHalf))
        while len(self.upperHalf) - len(self.lowerHalf) > 1:
            heapq.heappush_max(self.lowerHalf, heapq.heappop(self.upperHalf))

    def addNum(self, num: int) -> None:
        if self.upperHalf and num >= self.upperHalf[0]:
            heapq.heappush(self.upperHalf, num)
            self.rebalance_halves()
        else:
            heapq.heappush_max(self.lowerHalf, num)
            self.rebalance_halves()
        
    def findMedian(self) -> float:
        if len(self.lowerHalf) == len(self.upperHalf):
            return (self.lowerHalf[0] + self.upperHalf[0]) / 2
        elif len(self.lowerHalf) > len(self.upperHalf):
            return self.lowerHalf[0]
        else:
            return self.upperHalf[0]

        