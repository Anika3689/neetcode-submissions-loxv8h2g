class Solution:
    def isPalindrome(self, s: str, i, j, used: bool):
        if i >= j:
            return True
        
        if s[i] == s[j]:
            return self.isPalindrome(s, i+1, j-1, used)
        elif not used:
            return self.isPalindrome(s, i+1, j, True) or self.isPalindrome(s, i, j-1, True)
        return False

    def validPalindrome(self, s: str) -> bool:
        return self.isPalindrome(s, 0, len(s)-1, False)

