def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
    MOD = 1_000_000_007
    dp = [1] + [0]*maxLength
    for i in range(1, maxLength+1):
        if i >= oneGroup:
            dp[i] = (dp[i] + dp[i-oneGroup])%MOD
        if i >= zeroGroup:
            dp[i] = (dp[i] + dp[i-zeroGroup])%MOD
    return sum(dp[minLength:])%MOD