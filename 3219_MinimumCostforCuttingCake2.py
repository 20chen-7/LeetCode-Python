from typing import List
'''
think from 1D to 2D
'''
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        ans = i = j = 0 # i hor j ver
        while i < m - 1 or j < n - 1:
            if j == n - 1 or i < m - 1 and horizontalCut[i] > verticalCut[j]:
                ans += horizontalCut[i]* (j+1)
                i += 1
            else:
                ans += verticalCut[j] * (i+1)
                j += 1
        return ans