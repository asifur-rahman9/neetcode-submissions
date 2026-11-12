class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)

        grid = [[0] * (m+1) for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    grid[i][j] = grid[i-1][j-1] + 1
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])
                j+=1
            i+=1

        print(grid)
        return(grid[n][m])