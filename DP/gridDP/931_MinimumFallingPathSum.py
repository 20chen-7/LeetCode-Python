from cmath import inf
from typing import List


def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''
        j = 0,  dp[i][j] = min(dp[i-1][j], dp[i-1][j+1])+matrix[i][j]
        j = n -1 , dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])+matrix[i][j]
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])+matrix[i][j]
        '''
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        dp[0] = matrix[0]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[i][0] = min(dp[i-1][0], dp[i-1][1])+matrix[i][j]
                elif j  == n - 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])+matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])+matrix[i][j]
        return min(dp[-1])
'''
add more col
dp[i][j+1] = min(dp[i-1][j], dp[i-1][j+1], dp[i-1][j+2])+matrix[i][j]
dp[0][j+1] = matrix[0][j], dp[i][0] = dp[i][n-1] = inf
'''
def minFallingPathSum2(self, matrix: List[List[int]]) -> int:
        '''
        '''
        m, n = len(matrix), len(matrix[0])
        dp = [[inf]*(n+2) for _ in range(m)]
        dp[0][1:n+1] = matrix[0]
        for i in range(1, m):
            for j in range(n):
                    dp[i][j+1] = min(dp[i-1][j], dp[i-1][j+1], dp[i-1][j+2])+matrix[i][j]
        return min(dp[-1])
def minFallingPathSum3(self, matrix: List[List[int]]) -> int:
        '''
        '''
        m, n = len(matrix), len(matrix[0])
        dp = [inf]*(n+2)
        dp[1:n+1] = matrix[0]
        for i in range(1, m):
            pre = dp[0]
            for j in range(n):
                    pre, dp[j+1] = dp[j+1], min(pre, dp[j+1], dp[j+2])+matrix[i][j]
        return min(dp)