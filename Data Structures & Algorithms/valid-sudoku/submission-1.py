class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        numRows = len(board)
        rowElems = [set() for _ in range(numRows)]
        colElems = [set() for _ in range(numRows)]
        boxElems = {}
        for i in range(numRows // 3):
            for j in range(numRows // 3):
                boxElems[(i, j)] = set()
        
        for rowIdx in range(numRows):
            uniqueRowElems = rowElems[rowIdx]

            for colIdx in range(len(board[rowIdx])):
                currElem = board[rowIdx][colIdx]
                if currElem == '.':
                    continue
                currElem = int(currElem)
                if currElem < 1 or currElem > 9:
                    return False
            
                if currElem in uniqueRowElems:
                    return False
                uniqueRowElems.add(currElem)
                if currElem in colElems[colIdx]:
                    return False
                colElems[colIdx].add(currElem)

                uniqueBoxElems = boxElems[(rowIdx//3,colIdx//3)]
                if currElem in uniqueBoxElems:
                    return False
                uniqueBoxElems.add(currElem)
        
        return True

