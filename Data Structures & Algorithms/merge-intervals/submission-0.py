class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda interval : interval[0])
        non_overlapping = [intervals[0]]

        for i in range(1, len(intervals)):
            curStart, curEnd = intervals[i]
            prevStart, prevEnd = non_overlapping[-1]
            # If current interval is fully contained within previous
            if curStart >= prevStart and curEnd <= prevEnd:
                continue
            # If current interval starts within previous one but extends further
            elif curStart >= prevStart and curStart <= prevEnd:
                non_overlapping[-1][1] = curEnd 
            else:
                non_overlapping.append(intervals[i])
            

        return non_overlapping