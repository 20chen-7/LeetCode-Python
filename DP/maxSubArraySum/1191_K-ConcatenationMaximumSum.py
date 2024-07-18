'''
https://hackernoon.com/kadanes-algorithm-explained-50316f4fd8a6
Kadane's Algorithm
The max sum of subarray existed in single array, maxSum = #53
The max sum of subarray existed in two arrays, maxSum = maxPrefixSUM+maxPostfixSUM
The max sum of subarray existed in multiple arrays, maxSum = maxSingleArraySUM > 0, 
sum of (k-2) array + maxPrefixSUM+maxPostfixSUM
'''
from typing import List


MOD = 1_000_000_007
def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
    f = ans = 0
    for x in min(2, k)*arr:
        f = max(f, 0)+x
        ans = max(f, ans)
    return (ans if k == 1 else ans+max((k-2)*sum(arr), 0))%MOD