class Solution:
    def decodeString(self, s: str, left=0) -> str:
        res = ""
        i = left
        while i < len(s) and s[i] != ']':
            if s[i].isalpha():
                res += s[i]
                i += 1
                continue
            
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            k = int(s[start : i])

            subRes, i = self.decodeString(s, i + 1)
            res += k * subRes
            i += 1 # skip past the ']'

        if left == 0:
            return res

        return res, i
