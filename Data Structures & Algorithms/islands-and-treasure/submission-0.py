class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    step = 0
                    q.append((i, j, step))
                    
        while q: 
            r, c, step  = q.popleft()
            if r< 0 or c< 0 or c>=cols or r>=rows:
                continue
            if grid[r][c] == -1:
                continue
            if grid[r][c]> step:
                grid[r][c] = min(step, grid[r][c])
            elif not (grid[r][c] == 0 and step == 0):
                continue
            for dr, dc in directions:
                nr, nc = r+dr, c+ dc
                q.append((nr, nc, step+1))
        