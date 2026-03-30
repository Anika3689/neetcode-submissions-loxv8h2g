class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longestLen = 1
        maxElem = nums[0]
        minElem = nums[0]
        
        n = len(nums)
        l = 0

        for r in range(n):
            maxElem = max(nums[r], maxElem)
            minElem = min(nums[r], minElem)

            while abs(maxElem - minElem) > limit:
                l += 1
                maxElem = max(nums[l : r + 1])
                minElem = min(nums[l : r + 1])  
            
            # Now that window is valid, update longest length
            longestLen = max(longestLen, r - l + 1)
        
        return longestLen