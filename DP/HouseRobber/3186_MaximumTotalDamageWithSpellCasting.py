from typing import List
from collections import Counter
'''
2 can be replaced by k
'''

def maximumTotalDamage(self, power: List[int]) -> int:
    freq = Counter(power)
    a = sorted(freq.keys())
    j = 0
    dp = [0]*(len(a)+1)
    for i, x in enumerate(a):
        while a[j] < x - 2:
            j += 1
        dp[i+1] = max(dp[i], dp[j]+freq[x]*x)
    return dp[-1]
    