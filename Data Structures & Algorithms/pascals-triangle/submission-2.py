class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        
        for row in range(1, numRows):
            rowElems = [1]
            for i in range(1, row):
                rowElems.append(triangle[row-1][i-1] + triangle[row-1][i])
            rowElems.append(1)

            triangle.append(rowElems)

        return triangle