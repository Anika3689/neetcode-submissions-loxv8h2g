class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        indexSmallestAbs = 0
        for i in range(len(nums)):
            num = nums[i]
            absVal = abs(num)
            if absVal < abs(nums[indexSmallestAbs]):
                indexSmallestAbs = i
        
        res.append(nums[indexSmallestAbs] ** 2)
        l = indexSmallestAbs - 1
        r = indexSmallestAbs + 1

        while l >= 0 and r < len(nums):
            if abs(nums[l]) <= abs(nums[r]):
                res.append(nums[l] ** 2)
                l -= 1
            else:
                res.append(nums[r] ** 2)
                r += 1
        
        while l >= 0:
            res.append(nums[l] ** 2)
            l -= 1
        while r < len(nums):
            res.append(nums[r] ** 2)
            r += 1

        return res
        

        
