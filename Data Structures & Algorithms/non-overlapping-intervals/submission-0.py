class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for i in range(1, n):
            start, end = intervals[i]
            if start >= prevEnd:
                prevEnd = end
            else:
                prevEnd = min(prevEnd, end)
                res += 1
        
        return res