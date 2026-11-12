class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        order = []

        dic = defaultdict(list)

        for c, p in prerequisites:
            dic[c].append(p)

        unvisited, visiting, visited = 0, 1, 2

        states = [unvisited] * numCourses

        def dfs(node):
            state = states[node]
            if state == visiting:
                return False
            if state == visited:
                return True
            
            states[node] = visiting

            for nei in dic[node]:
                if not dfs(nei):
                    return False
            order.append(node)

            states[node] = visited

            return True


        for i in range(numCourses):
            if not dfs(i):
                return []

        return order
