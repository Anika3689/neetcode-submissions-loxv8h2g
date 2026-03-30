class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redCount = 0
        whiteCount = 0
        blueCount = 0
        for num in nums:
            if num == 0:
                redCount += 1
            elif num == 1:
                whiteCount += 1
            else:
                blueCount += 1
        
        print(redCount)
        print(whiteCount)
        print(blueCount)

        for i in range(redCount):
            nums[i] = 0
        for i in range(redCount, redCount + whiteCount):
            nums[i] = 1
        for i in range(redCount + whiteCount, redCount + whiteCount + blueCount):
            nums[i] = 2