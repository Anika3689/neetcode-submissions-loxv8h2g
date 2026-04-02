class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        wellFormedParens = []

        def helper(curString: str, nOpen: int, nClose: int):
            if nOpen == nClose == 0:
                wellFormedParens.append(curString)
                return

            if nOpen > 0:
                helper(curString + '(', nOpen - 1, nClose)
            if nClose > nOpen:
                helper(curString + ')', nOpen, nClose - 1)

        helper('', n, n)
        return wellFormedParens
        
        
      