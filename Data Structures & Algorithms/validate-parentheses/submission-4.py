class Solution:
    def isValid(self, s: str) -> bool:
        parensMapping = {'{' : '}', '(' : ')', '[' : ']'}
        stk = []
        for i in range(len(s)):
            # If character is open paren:
            if s[i] in parensMapping:
                stk.append(s[i])
                continue

            if stk and parensMapping[stk[-1]] == s[i]:
                stk.pop()
            else:
                return False
        
        return len(stk) == 0
            
