class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1], [-1,0],[0,-1]]

        rows = len(grid)
        cols = len(grid[0])


        fresh = 0
        time = 0

        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh +=1

                if grid[i][j] == 2:
                    q.append([i, j])

        while q and fresh>0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if  row<0 or col<0 or row == rows or col == cols or grid[row][col] != 1:
                        continue

                    grid[row][col] = 2
                    fresh -=1
                    q.append([row, col])
            time+=1

        if fresh == 0:
            return time
        else:
            return -1 

