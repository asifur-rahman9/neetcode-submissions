class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        directions  = [(1,0),(0, 1),(-1, 0),(0, -1)]
        visited = set()
        
        def dfs(i,j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return

            if (i,j) in visited:
                return
            if board[i][j] == "X":
                return

            visited.add((i,j))

            for dr, dc in directions:
                r, c = i+dr, j+ dc
                dfs(r, c)
                
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m -1:
                    dfs(i ,j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"


        
