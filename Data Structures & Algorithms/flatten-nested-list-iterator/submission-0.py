class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))

    def next(self) -> int:
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.stack and not self.stack[-1].isInteger():
            lst = self.stack.pop().getList()
            while lst:
                self.stack.append(lst.pop())
        
        return len(self.stack) > 0