class StringIterator:

    def __init__(self, compressedString: str):
        self.compressedArr = list(compressedString)
        self.i = 0 
        self.nextLetterIndex = None
        self.curRemaining = None
        self._readNextCount()

    def _readNextCount(self):
        # Get the total count for the next letter
        self.nextLetterIndex = self.i + 1
        while self.nextLetterIndex < len(self.compressedArr) and self.compressedArr[self.nextLetterIndex].isdigit():
            self.nextLetterIndex += 1
        self.curRemaining = int(''.join(self.compressedArr[self.i + 1 : self.nextLetterIndex]))

    def next(self) -> str:
        if self.i >= len(self.compressedArr):
            return ' '
        # if there are more copies of the current character to expand
        if self.curRemaining > 0:
            self.curRemaining -= 1
            return self.compressedArr[self.i]

        self.i = self.nextLetterIndex
        self._readNextCount()
        self.curRemaining -= 1
        return self.compressedArr[self.i]

    def hasNext(self) -> bool:
        if self.i >= len(self.compressedArr):
            return False    
        return True


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
