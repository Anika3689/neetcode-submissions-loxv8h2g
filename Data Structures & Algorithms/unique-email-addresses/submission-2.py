class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seenEmails = set()
        for mail in emails:
            localName = ''
            i = 0
            while mail[i] != '@':
                ch = mail[i]
                if ch == '+':
                    break
                if ch != '.':
                    localName += ch
                i += 1
            
            while mail[i] != '@':
                i += 1

            seenEmails.add(localName + mail[i:])

        return len(seenEmails)