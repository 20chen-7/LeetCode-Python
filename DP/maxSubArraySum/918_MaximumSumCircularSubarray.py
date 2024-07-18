from math import inf
from typing import List
'''
1. subarray in single array
    #53
    maxS
    
2. two end in single array
    sum(nums)-minS
    
3. whole array
    [-9,-9,1,1,-9,-9]
    minS == sum(nums), return maxS, minS can't be whole array
TC: O(N)
SC: O(1)
'''

def maxSubarraySumCircular(self, nums: List[int]) -> int:
    min_s = 0
    max_s = -inf #can 't be empty
    min_f = 0
    max_f = 0
    for x in nums:
        min_f = min(min_f, 0)+x
        max_f = max(max_f, 0)+x
        max_s = max(max_s, max_f)
        min_s = min(min_s, min_f)
    if min_s == sum(nums):
        return max_s
    return max(max_s, sum(nums)-min_s)