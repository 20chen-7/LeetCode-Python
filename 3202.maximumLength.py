'''
Memoization Search unnecessary

Recursion

$7.2 topic DP

'''




'''
(a+b)%k == (b+c)%k
mean => a%k = c%k
b%k = d%k
first/last two num in the sub array enough

multi-thread
C(nk+k^2)
'''
def maximumLength(nums, k):
    dp = [[0]*k for _ in range(k)]
    for x in nums:
        x%=k
        for y in range(k):
            dp[y][x] = dp[x][y]+1
    return max(map(max, dp))

'''
C(nk+n^2)
'''
def maximumLength2(nums, k):
    n = len(nums)
    dp = [[1]*k for _ in range(n)]
    ans = 2
    for i in range(1, n):
        for j in range(i):
            dp[i][(nums[i]+nums[j])%k] = dp[j][(nums[i]+nums[j])*k]+1
            ans = max(dp[i][(nums[i]+nums[j])%k], ans)  
    return ans  
'''
prossible due to mod is slow for python
C(nk+k^2)
'''
def maximumLength3(nums, k):
    ans = 0
    for m in range(k):
        f = [0]*k
        for x in nums:
            x%=k
            f[x] = f[(m-x)%k]+1
        ans = max(ans, max(f))
    return ans 
'''
3201 is k = 2

'''