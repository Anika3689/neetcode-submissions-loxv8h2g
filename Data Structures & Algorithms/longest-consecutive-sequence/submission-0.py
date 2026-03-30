class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        globalMaxLen = 1
        localMaxLen = 1
        prevInSeqElem = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == prevInSeqElem:
                continue
            if nums[i] == prevInSeqElem + 1:
                localMaxLen += 1
            else:
                #Streak is broken
                globalMaxLen = max(globalMaxLen, localMaxLen)
                localMaxLen = 1
            prevInSeqElem = nums[i]
        
        globalMaxLen = max(globalMaxLen, localMaxLen)
        return globalMaxLen