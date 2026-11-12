class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        m = defaultdict(list)

        for c, p in prerequisites:
            m[c].append(p)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED]  * numCourses

        def dfs(node):
            state = states[node] 
            if state == VISITED:
                return True
            if state == VISITING:
                return False

            states[node] = VISITING

            for nei in m[node]:
                if not dfs(nei):
                    return False
            
            states[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        