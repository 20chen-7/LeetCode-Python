from typing import List


def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0]*(n+1) for _ in range(m+1)]
        f[1][1] = 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j == 1:
                    continue
                if obstacleGrid[i-1][j-1] == 1:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i][j-1] + f[i-1][j]
        return f[-1][-1]
def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j+1] = 0
                else:
                    dp[j+1] += dp[j]
        return dp[-1]