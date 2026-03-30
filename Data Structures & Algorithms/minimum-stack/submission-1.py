class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.minStk) == 0 or val <= self.minStk[-1]:
            self.minStk.append(val) 

    def pop(self) -> None:
        top_elem = self.stk.pop()
        if self.minStk[-1] == top_elem:
            self.minStk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]
