class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda interval: interval[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            curStart, curEnd = intervals[i]
            prevStart, prevEnd = merged[-1]
            if curStart <= prevEnd:
                merged[-1][1] = max(prevEnd, curEnd)
            else:
                merged.append(intervals[i])
        
        return merged