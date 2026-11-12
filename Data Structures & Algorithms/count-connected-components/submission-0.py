class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)

        total = 0

        for i in range(n):
            if i not in visited:
                total+=1
                dfs(i)
        
        return total


        