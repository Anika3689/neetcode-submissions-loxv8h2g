class MyCircularQueue:

    def __init__(self, k: int):
        self.r = 0 
        self.w = 0
        self.queue = [-1] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.w] = value
        self.w = (self.w + 1) % len(self.queue)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.r] = -1
        self.r = (self.r + 1) % len(self.queue)
        return True

    def Front(self) -> int:
        return self.queue[self.r]

    def Rear(self) -> int:
        return self.queue[(self.w - 1) % len(self.queue)]

    def isEmpty(self) -> bool:
        return self.r == self.w and self.queue[self.w] == -1

    def isFull(self) -> bool:
        return self.r == self.w and self.queue[self.w] != -1
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()