class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0

        while l < r:
            leftHeight = height[l]
            rightHeight = height[r]
            maxArea = max(maxArea, min(leftHeight, rightHeight) * (r-l))

            #Left line of current boundary is shorter
            if leftHeight < rightHeight:
                l += 1
            else:
                r -= 1
    
        return maxArea