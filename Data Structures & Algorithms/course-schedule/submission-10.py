class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        visited = set()
        path = set ()

        for post, pre in prerequisites:
            graph[pre].append(post)

        def dfs(node):
            if node in visited:
                return True
            if node in path:
                return False

            path.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            path.add(node)

            visited.add(node)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        

