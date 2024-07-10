'''
10, i = 0, dfs(i) = min(dfs(i-2)+cost[i-2], dfs(i-1) + cost[i])
dp[0] = 0
dp[1] = 0
dp[2] = min(dp[0], dp[1])+cost[i]

i = 1 

'''
def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0]*(n+1)
    for i in range(2, n+1):
        dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    return dp[n]

def minCostClimbingStairs(cost):
    n = len(cost)
    p1 = p0 = 0
    for i in range(2, n+1):
        new_P = min(p0+cost[i-2], p1+cost[i-1])
        p0 = p1
        p1 = new_P
    return p1
