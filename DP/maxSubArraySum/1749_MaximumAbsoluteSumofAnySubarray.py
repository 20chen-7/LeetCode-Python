from itertools import accumulate
from typing import List
'''
TC: O(N)
SC: O(1)
'''

def maxAbsoluteSum(self, nums: List[int]) -> int:
    f_min = f_max = ans = 0
    for x in nums:
        f_min = min(f_min, 0)+x
        f_max = max(f_max, 0)+x
        ans = max(f_max, -f_min, ans)
    return ans
'''
prefix sum,
TC: O(N)
SC: O(N)
'''
def maxAbsoluteSum2(self, nums: List[int]) -> int:
    s = list(accumulate(nums, initial=0))
    return max(s) - min(s)

