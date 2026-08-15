class Solution:
    def decodeString(self, s: str, l=None, r=None) -> str:
        if l is None:
            l = 0
        if r is None:
            r = len(s)

        res = ""
        i = l
        while i < r:
            if not s[i].isdigit():
                res += s[i]
                i += 1
                continue

            l = i
            while i < r and s[i].isdigit():
                i += 1
            k = int(s[l:i])

            i += 1
            l = i
            numOpenSeen = 1

            while i < r and not (numOpenSeen == 1 and s[i] == ']'):
                if s[i] == '[':
                    numOpenSeen += 1
                if s[i] == ']':
                    numOpenSeen -= 1
                i += 1

            res += self.decodeString(s, l, i) * k
            i += 1
        
        return res