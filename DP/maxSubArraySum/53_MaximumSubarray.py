from math import inf
from typing import List
'''
TC: O(N)
SC: O(1)
'''

def maxSubArray(self, nums: List[int]) -> int:
    prefix = 0
    minPrex = 0
    ans = -inf
    for x in nums:
        prefix += x
        ans = max(prefix-minPrex, ans)
        minPrex = min(prefix, minPrex)
    return ans
'''
dp
f[i] => max sum of subarray
can be nums[i], max(f[i-1],0)+nums[i]
TC: O(N)
SC: O(N)
'''
def maxSubArray2(self, nums: List[int]) -> int:
    dp = [0]*(len(nums))
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1], 0)+nums[i]
    return max(dp)
'''
TC: O(N)
SC: O(1)
'''
def maxSubArray3(self, nums: List[int]) -> int:
    ans = -inf
    f = 0
    for x in nums:
        f = max(f, 0)+x
        ans = max(ans, f)
    return ans