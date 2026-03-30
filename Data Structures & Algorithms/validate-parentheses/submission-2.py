class Solution:
    def isValid(self, s: str) -> bool:
        parensMapping = {')' : '(', 
                        '}' : '{', 
                        ']' : '['}
        openParens = parensMapping.values()

        stk = []
        for paren in s:
            if paren in openParens:
                stk.append(paren)
                continue
            try:
                top = stk.pop()
                if top != parensMapping[paren]:
                    return False
            except:
                return False
        
        return len(stk) == 0

