class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        nRows = len(picture)
        nCols = len(picture[0])

        rowBlackPositions = defaultdict(set)
        colBlackPositions = defaultdict(set)

        for rowIdx in range(nRows):
            blackSpots = set()
            for colIdx in range(nCols):
                if picture[rowIdx][colIdx] == 'B':
                    pos = (rowIdx, colIdx)
                    colBlackPositions[colIdx].add(pos) 
                    blackSpots.add(pos)
            rowBlackPositions[rowIdx] = blackSpots
        
        lonelyBlackCt = 0
        for rowIdx in range(nRows):
            for colIdx in range(nCols):
                val = picture[rowIdx][colIdx]
                if val == 'B' and len(rowBlackPositions[rowIdx]) == 1 and len(colBlackPositions[colIdx]) == 1:
                    lonelyBlackCt += 1
        
        return lonelyBlackCt