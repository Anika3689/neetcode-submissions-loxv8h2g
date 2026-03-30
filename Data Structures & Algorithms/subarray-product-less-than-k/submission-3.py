class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # numbers are always positive integers
        if k <= 1:
            return 0
        res = 0
        prod = 1
        n = len(nums)
        l = 0
        for r in range(n):
            prod *= nums[r]
            while l < n and prod >= k:
                prod /= nums[l]
                l += 1
            
            if prod < k:
                res += r - l + 1
        
        return res


