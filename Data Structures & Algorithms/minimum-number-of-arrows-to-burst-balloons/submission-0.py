class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        prevEnd = points[0][1]
        minArrows = 1

        for i in range(1, len(points)):
            curStart, curEnd = points[i]
            if curStart <= prevEnd:
                prevEnd = min(prevEnd, curEnd)
            else:
                minArrows += 1
                prevEnd = curEnd
        
        return minArrows