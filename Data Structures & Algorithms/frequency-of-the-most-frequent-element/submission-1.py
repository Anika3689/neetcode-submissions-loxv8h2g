class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFreq = 0
        windowSum = 0
        l, r = 0, 0

        for r in range(len(nums)):
            windowSum += nums[r]
            # Shrink window while k increments isn't enough for all elems to reach nums[r]:
            while windowSum + k < nums[r] * (r - l + 1):
                windowSum -= nums[l]
                l += 1

            # Now that the window is valid
            maxFreq = max(maxFreq, r - l + 1)
            
        return maxFreq
            

