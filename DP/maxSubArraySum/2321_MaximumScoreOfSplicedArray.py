'''
maximize difference subS
TC: O(N)
SC: O(1)
'''

from typing import List


def maxS(self, nums1, nums2):
    max_s = s = 0
    for x, y in zip(nums1, nums2):
        s = max(s+y-x, 0)
        max_s = max(s, max_s)
    return sum(nums1)+max_s
def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
    return max(maxS(nums1, nums2), maxS(nums2, nums1))