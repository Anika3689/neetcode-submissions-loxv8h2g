class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        curMax = 0

        while l < r:
            width = r - l
            if height[l] <= height[r]:
                curMax = max(curMax, height[l] * width)
                l += 1
            else:
                curMax = max(curMax, height[r] * width)
                r -= 1
        
        return curMax