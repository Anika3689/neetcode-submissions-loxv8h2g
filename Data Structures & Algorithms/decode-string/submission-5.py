class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        decoded = ""
        i = 0
        while i < len(s):
            l = i
            while s[i].isdigit():
                i += 1
            if i > l:
                stk.append([int(s[l:i]), ""])

            if s[i] == ']':
                k, substr = stk.pop()
                if stk:
                    stk[-1][1] += k * substr
                else:
                    decoded += k * substr
            elif s[i] != '[':
                if stk:
                    stk[-1][1] += s[i]
                else:
                    decoded += s[i]

            i += 1

        return decoded
            

            
