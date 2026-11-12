class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]

        best = 0
        count = 0


        def dfs(r, c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == 0:
                return 0

            if (r,c) in visited:
                return 0

            visited.add((r,c))
            area = 1

            for dr in directions:
                area += dfs(r+dr[0], c+dr[1])

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    best= max(best, dfs(r,c))

        return best

        