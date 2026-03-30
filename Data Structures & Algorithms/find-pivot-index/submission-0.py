class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        prefixSums = [0 for _ in range(n)]
        for i in range(1, n):
            prefixSums[i] = nums[i-1] + prefixSums[i-1]
        
        suffixSums = [0 for _ in range(n)]
        for i in range(n-2, -1, -1):
            suffixSums[i] = nums[i+1] + suffixSums[i+1]
        
        for i in range(n):
            if prefixSums[i] == suffixSums[i]:
                return i
        return -1