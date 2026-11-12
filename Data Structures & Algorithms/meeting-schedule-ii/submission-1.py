"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)

        rooms = []


        for m in intervals:
            if rooms and rooms[0]<=m.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, m.end)

        return len(rooms)
            

        