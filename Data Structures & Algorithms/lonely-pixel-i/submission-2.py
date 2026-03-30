class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        nRows = len(picture)
        nCols = len(picture[0])

        rowBlackPositions = defaultdict(int)
        colBlackPositions = defaultdict(int)

        for rowIdx in range(nRows):
            blackSpots = 0
            for colIdx in range(nCols):
                if picture[rowIdx][colIdx] == 'B':
                    pos = (rowIdx, colIdx)
                    colBlackPositions[colIdx] += 1 
                    blackSpots += 1
            rowBlackPositions[rowIdx] = blackSpots
        
        lonelyBlackCt = 0
        for rowIdx in range(nRows):
            for colIdx in range(nCols):
                val = picture[rowIdx][colIdx]
                if val == 'B' and rowBlackPositions[rowIdx] == 1 and colBlackPositions[colIdx] == 1:
                    lonelyBlackCt += 1
        
        return lonelyBlackCt