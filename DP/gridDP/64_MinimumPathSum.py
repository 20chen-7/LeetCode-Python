from typing import List


def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]* n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i][j-1]+x, dp[i-1][j]+x)
                elif i > 0 :
                    dp[i][j] = dp[i-1][j]+x
                elif j > 0:
                    dp[i][j] = dp[i][j-1]+x
        return dp[-1][-1]
    
def minPathSum2(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        dp = [0]* n
        dp[0] = grid[0][0]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if i > 0 and j > 0:
                    dp[j] = min(dp[j-1]+x, dp[j]+x)
                elif i > 0 :
                    dp[j] += x
                elif j > 0:
                    dp[j] = dp[j-1]+x
        return dp[-1]
    
def minPathSum3(self, grid: List[List[int]]) -> int:

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if i > 0 and j > 0:
                    grid[0][j] = min(grid[0][j-1]+x, grid[0][j]+x)
                elif i > 0 :
                    grid[0][j] += x
                elif j > 0:
                    grid[0][j] = grid[0][j-1]+x
        return grid[0][-1]