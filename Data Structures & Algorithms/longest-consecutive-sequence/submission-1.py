class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
            
        longestLen = 1
        nums = set(nums)

        for startNum in nums:
            if startNum - 1 in nums:
                continue
            curSeqLen = 1
            num = startNum
            while num + 1 in nums:
                num += 1
                curSeqLen += 1
            
            longestLen = max(longestLen, curSeqLen)
        
        return longestLen