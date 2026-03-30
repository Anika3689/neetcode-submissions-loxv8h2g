class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxStreak = 0
        curStreak = 0
        for num in nums:
            if num == 1:
                curStreak += 1
                maxStreak = max(curStreak, maxStreak)
            else:
                curStreak = 0
        
        return maxStreak