class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        res = []
        # for i in range(len(heap)):
        #     res.append(heapq.heappop(heap))
        return heap[0]


        