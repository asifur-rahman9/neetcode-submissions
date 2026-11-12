"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

[(5,10),(15,20),(0,40)]
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        heap = []

        for m in intervals:
            if heap and heap[0]<=m.start:
                heapq.heappop(heap)
            heapq.heappush(heap, m.end)

        return len(heap)

            





        