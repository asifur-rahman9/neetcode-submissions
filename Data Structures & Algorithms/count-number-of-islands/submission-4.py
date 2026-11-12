class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        
        def bfs(i, j):
            q.append((i, j))
            

            while q:
                r, c = q.popleft()
                if r<0 or c<0 or c>cols-1 or r> rows-1:
                    continue

                if (r, c) in visited:
                    continue
                if grid[r][c] == "0":
                    continue
                
                visited.add((r, c))

                for dr, dc in directions:
                    nr, nc = r+dr, dc+ c
                    q.append((nr, nc)) 

            return 1

 
        total = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited and 0<=i<rows and 0<=j<cols:
                    total += bfs(i, j)

        return total


        
