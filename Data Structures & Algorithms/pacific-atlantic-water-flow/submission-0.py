class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        res = []
       
        def bfs(r,c):
            visited = {(r, c)}
            q = deque([(r, c)])
            atl = pac = False
            while q:
                r, c = q.popleft()

                if r==0 or c==0:
                    pac = True

                if r==rows-1 or c==cols-1:
                    atl = True

                if atl and pac:
                    return True

                for dr, dc in directions:
                    nr, nc = dr+r, dc+c

                    if (nr, nc) not in visited and 0 <= nr < rows and 0 <= nc < cols and heights[r][c]>=heights[nr][nc]:
                        q.append((nr, nc))
                        visited.add((nr, nc))

            return False


        for i in range(rows):
            for j in range(cols):
                if bfs(i, j):
                    res.append([i, j])
        
        return res
        