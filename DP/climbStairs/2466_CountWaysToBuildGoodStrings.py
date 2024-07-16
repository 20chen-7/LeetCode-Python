'''
empty string dp[0] = 1
TC: O(high)
SC: O(high)
'''
def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
    dp = [1] + high*[0]
    MOD = 1_000_000_007
    for i in range(1, high+1):
        if i >= zero:
            dp[i] = (dp[i] + dp[i-zero])%MOD
        if i >= one:
            dp[i] = (dp[i] + dp[i-one])%MOD
    return sum(dp[low:])%MOD