class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited = set()
        path = set()
        res = []

        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a) 

        def dfs(node):
            if node in visited:
                return True
            if node in path:
                return False

            path.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
                
            path.remove(node)
            
            visited.add(node)
            res.append(node)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        res.reverse()
        return res
    