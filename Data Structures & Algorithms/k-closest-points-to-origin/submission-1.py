class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = []

        for start, end in points:
            distance = math.sqrt((start - 0)**2 + (end - 0)**2)
            heapq.heappush(self.heap, (distance, start, end))
        res = []
        for _ in range(k):
            distance, start, end = heapq.heappop(self.heap)
            res.append([start, end])

        return res

