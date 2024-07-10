''''
    n
n-1, n-2
... ... 
0, 1 .... 
memorization search
bottom-top
dfs[i] = dfs[i-1]+dfs[i-2]
i <= 1: return 1
i = 0, or i = 1, only 1
'''
def climbStairs(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(1, n):
        dp[i+1] = dp[i]+dp[i-1]
    return dp[n]