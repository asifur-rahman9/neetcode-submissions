class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for start, end, cost in times:
            graph[start].append((end, cost))

        heap = [(0, k)]
        times = {}

        while heap:
            cost, des = heapq.heappop(heap)
            if des in times:
                continue
            times[des] = cost

            for nei, c in graph[des]:
                if nei not in times:
                    heapq.heappush(heap, (cost+c, nei))

        print(times)

        if len(times) == n:
            return max(times.values())
        else:
            return -1


