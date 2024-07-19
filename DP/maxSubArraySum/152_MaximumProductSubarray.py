from cmath import inf
from typing import List
'''
negative cases, require local min
'''

def maxProduct(self, nums: List[int]) -> int:
    fmin = fmax = pmax = pmin = 1
    ans = -inf
    for x in nums:
        fmax = max(pmin*x, pmax*x, x)
        fmin = min(pmin*x, pmax*x, x)
        pmax, pmin = fmax, fmin
        ans = max(fmax, ans)
    return ans