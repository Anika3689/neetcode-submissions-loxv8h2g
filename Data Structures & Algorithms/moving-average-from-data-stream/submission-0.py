class MovingAverage:

    def __init__(self, size: int):
        self.maxSize = size
        self.queue = deque([])
        self.Sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.Sum += val
        if len(self.queue) > self.maxSize:
            self.Sum -= self.queue.popleft()

        return self.Sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
