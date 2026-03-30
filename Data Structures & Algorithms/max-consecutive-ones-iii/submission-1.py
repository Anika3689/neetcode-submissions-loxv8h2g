class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curNumZeros = 0
        maxWindowLen = 0
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] == 0:
                curNumZeros += 1
            
            while l <= r and curNumZeros > k:
                if nums[l] == 0:
                    curNumZeros -= 1
                
                l += 1

            maxWindowLen = max(maxWindowLen, r - l + 1)
        
        return maxWindowLen
                
