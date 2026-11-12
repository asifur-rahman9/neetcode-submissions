class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        best = 0



        def dfs(r, c):
            if r<0 or c< 0 or r>rows-1 or c>cols-1:
                return 0
            if (r, c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r, c))
            area = 1

            for dr, dc in directions:
                area += dfs(dr+r, dc+c)
            return area
                

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j)not in visited:
                    best = max(dfs(i, j), best)

        return best
