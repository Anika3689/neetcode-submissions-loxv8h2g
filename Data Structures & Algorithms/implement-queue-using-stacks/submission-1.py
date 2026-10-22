class MyQueue:

    def __init__(self):
        self.writeTo = []
        self.readFrom = []

    def push(self, x: int) -> None:
        self.writeTo.append(x)

    # helper for pop() and peek()
    def populateReadStack(self):
        while self.writeTo:
            self.readFrom.append(self.writeTo.pop())

    def pop(self) -> int:
        if len(self.readFrom) == 0:
            self.populateReadStack()
        return self.readFrom.pop()
        
    def peek(self) -> int:
        if len(self.readFrom) == 0:
            self.populateReadStack()
        return self.readFrom[-1]

    def empty(self) -> bool:
        return len(self.writeTo) + len(self.readFrom) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()