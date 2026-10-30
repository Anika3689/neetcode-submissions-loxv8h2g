"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)
        minRooms = 0
        # holds previously started meetings
        # used to access the meeting that ends earliest
        activeMeetings = [] 
        for i in range(len(intervals)):
            while activeMeetings and activeMeetings[0] <= intervals[i].start:
                heapq.heappop(activeMeetings)

            heapq.heappush(activeMeetings, intervals[i].end)
            minRooms = max(minRooms, len(activeMeetings))
            
        
        return minRooms



