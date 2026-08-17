class Solution:
    def decodeString(self, s: str, left=0) -> str:
        num = ""
        stack = []
        res = ""

        for ch in s:
            if ch.isdigit():
                num += ch
                continue
            
            if ch == '[':
                stack.append([int(num), ""])
                num = ""
            elif ch.isalpha():
                if not stack:
                    res += ch
                else:
                    stack[-1][1] += ch
            else:
                # ch is ']'
                k, curDecoded = stack.pop()
                if not stack:
                    res += k * curDecoded
                else:
                    stack[-1][1] += k * curDecoded

        return res


            
