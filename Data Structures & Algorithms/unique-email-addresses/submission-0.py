class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seenEmails = set()
        for mail in emails:
            localName, domain = mail.split('@')
            localNameParsed = ''
            for ch in localName:
                if ch == '+':
                    break
                if ch != '.':
                    localNameParsed += ch
            seenEmails.add(localNameParsed + '@' + domain)

        return len(seenEmails)