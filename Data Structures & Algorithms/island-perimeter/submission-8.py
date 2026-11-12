class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()



        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1       # crossed into water or off the grid: one edge
            if (i, j) in visited:
                return 0       # already counted this land cell
            visited.add((i, j))
            perimeter = dfs(i, j+1)
            perimeter += dfs(i+1, j)
            perimeter += dfs(i, j-1)
            perimeter += dfs(i-1, j)       
            return perimeter
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i, j)

        return 0