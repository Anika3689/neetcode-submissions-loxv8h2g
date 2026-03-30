class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += (str(len(word)) + '#' + word)
        return encoded

    def findNextCount(self, s: str, i: int):
        count = ''
        while i < len(s) and s[i] != '#':
            if s[i].isdigit():
                count += s[i]
            i += 1
        return int(count), i+1

    def decode(self, s: str) -> List[str]:
        decoded = []
        curWord = ""
        numCharsLeft = None
        i = 0
        if not s:
            return decoded

        while i < len(s):
            ch = s[i]
            if numCharsLeft is None:
                numCharsLeft, i = self.findNextCount(s, i)
            elif numCharsLeft == 0:
                decoded.append(curWord)
                curWord = ''
                numCharsLeft, i = self.findNextCount(s, i)
            else:
                curWord += ch
                numCharsLeft -= 1
                i += 1

        decoded.append(curWord)
        return decoded
        
