class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        m = defaultdict(list)


        for c, p in prerequisites:
            m[c].append(p)

        visited = set()

        def dfs(course):
            if m[course] == []:
                return True

            if course in visited:
                return False

            visited.add(course)
            for prereq in m[course]:
                if not dfs(prereq):
                    return False
            m[c] = []
            visited.remove(course)
            return True

        for c, p in prerequisites:
            if not dfs(c):
                return False
        return True


        