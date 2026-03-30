class Solution:

    def generateAll(self, curStr, numOpenUsed=0, numCloseUsed=0):
        if self.n == numOpenUsed == numCloseUsed:
            self.allResults.append(curStr)
            return
        
        if numCloseUsed == numOpenUsed:
            self.generateAll(curStr + '(', numOpenUsed + 1, numCloseUsed)
        elif numOpenUsed == self.n:
            self.generateAll(curStr + ')', numOpenUsed, numCloseUsed + 1)
        else:
            self.generateAll(curStr + '(', numOpenUsed + 1, numCloseUsed)
            self.generateAll(curStr + ')', numOpenUsed, numCloseUsed + 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.allResults = []
        self.generateAll('(', 1, 0)
        return self.allResults