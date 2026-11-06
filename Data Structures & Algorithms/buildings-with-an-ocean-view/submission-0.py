class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        oceanViews = [len(heights)-1]
        maxHeight = heights[-1]

        for i in range(len(heights)-2, -1, -1):
            if heights[i] > maxHeight:
                oceanViews.append(i)
                maxHeight = heights[i]
        
        oceanViews.reverse()
        return oceanViews