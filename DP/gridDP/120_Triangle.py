from typing import List


def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        dp[0][0] = triangle[0][0] 
        i -> 1, n, j<i+1
        dp[i][j] = min(dp[i-1][j], dp[i-1][j+1])+triangle[i][j]
        '''
        n = len(triangle)
        dp = [[0]* len(x) for x in triangle]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j]+triangle[i][j]
                elif j >=i:
                    dp[i][j] = dp[i-1][j-1]+triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1])+triangle[i][j]
                
        return min(dp[-1])
    
def minimumTotal2(self, triangle: List[List[int]]) -> int:
        '''
        dp[0][0] = triangle[0][0] 
        i -> 1, n, j<i+1
        dp[i][j] = min(dp[i-1][j], dp[i-1][j+1])+triangle[i][j]
        '''
        n = len(triangle)
        dp = [0]* (n)
        for i in range(n):
            dp[i] = triangle[-1][i]
        for i in range(n-2, -1,-1):
            for j in range(i+1):
                    dp[j] = min(dp[j], dp[j+1])+triangle[i][j]
                
        return dp[0]

