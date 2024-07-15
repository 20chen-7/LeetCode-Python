'''
    3,  4,  2
   0,   2,  4
'''
import collections


def deleteAndEarn(nums):
    numsMap = collections.Counter(nums)
    maxL = max(numsMap.keys())
    dp = [0]*(maxL+1)
    dp[1] = 1*numsMap[1]
    for i in range(2, maxL+1):
        dp[i] = max(dp[i-1], dp[i-2]+i*numsMap[i])
    return dp[-1]
def deleteAndEarn2(nums):
    numsMap = collections.Counter(nums)
    maxL = max(numsMap.keys())
    first, second = 0, 1*numsMap[1]
    for i in range(2, maxL+1):
        first, second = second, max(second, first+i*numsMap[i])
    return second
    
        