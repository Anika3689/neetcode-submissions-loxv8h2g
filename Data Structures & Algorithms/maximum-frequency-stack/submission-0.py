class FreqStack:

    def __init__(self):
        self.valsToFreqs = {}
        self.freqsToVals = []

    def push(self, val: int) -> None:
        if val in self.valsToFreqs:
            self.valsToFreqs[val] += 1
        else:
            self.valsToFreqs[val] = 1
        
        freq = self.valsToFreqs[val]
        if freq - 1 >= len(self.freqsToVals):
            self.freqsToVals.append([])
        
        self.freqsToVals[freq - 1].append(val)
        

    def pop(self) -> int:
        maxFreq = len(self.freqsToVals) - 1
        while maxFreq >= 0 and len(self.freqsToVals[maxFreq]) == 0:
            maxFreq -= 1

        poppedVal = self.freqsToVals[maxFreq].pop() 
        
        if self.valsToFreqs[poppedVal] - 1 == 0:
            self.valsToFreqs.pop(poppedVal)
        else:
            self.valsToFreqs[poppedVal] -= 1

        return poppedVal

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()