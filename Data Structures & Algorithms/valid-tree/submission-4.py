class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()

        if len(edges) != (n-1):
            return False

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)   

        def dfs(node):
            
            if node in visited:
                return False
            visited.add(node)
            print(visited)

            for nei in graph[node]:
                print(nei)
                dfs(nei)
            return True
        
        dfs(0)
        return len(visited) == n
            



        

        