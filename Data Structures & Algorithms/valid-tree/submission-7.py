class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited =set()

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)

            for nei in graph[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n
