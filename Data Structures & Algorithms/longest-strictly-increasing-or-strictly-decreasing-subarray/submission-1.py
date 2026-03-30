class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longestInc = 1
        longestDec = 1

        curIncLen = 1
        curDecLen = 1

        for i in range(1, len(nums)):
            curNum = nums[i]
            if curNum > nums[i - 1]:
                curIncLen += 1
                curDecLen = 1
            elif curNum < nums[i - 1]:
                curDecLen += 1
                curIncLen = 1
            else:
                curIncLen = 1
                curDecLen = 1
            
            longestInc = max(longestInc, curIncLen)
            longestDec = max(longestDec, curDecLen)
        
        return max(longestInc, longestDec)
            


            
