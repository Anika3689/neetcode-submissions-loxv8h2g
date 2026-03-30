# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        guessed = n // 2
        left, right = 1, n
        while left <= right:
            response = guess(guessed)
            if response == 0:
                return guessed
            elif response == -1:
                right = guessed - 1
            else:
                left = guessed + 1
            
            guessed = (left + right) // 2
        
        return -1