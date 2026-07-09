class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longestStreak = 0
        numZeros = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                numZeros += 1

            while numZeros > k:
                if nums[l] == 0:
                    numZeros -= 1
                l += 1
            
            longestStreak = max(longestStreak, r - l + 1)
        
        return longestStreak