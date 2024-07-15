from typing import List
'''
think from 1D to 2D
cost_h0 = (#vertical cuts + 1) * h0 + previous cost
cost_v0 = (#horizontal cuts + 1) * v0 + previous cost
greedy
h -> v (#vertical cuts + 1) * h + (#horizontal cuts + 2) * v 
v -> h (#horizontal cuts + 1) * v + (#vertical cuts + 2) * h
chose smaller one
TC: O(mlogm+nlogn)
SC: O(1)
'''
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        ans = i = j = 0 # i hor j ver
        cntV = cntH = 1
        while i < m - 1 or j < n - 1:
            if j == n - 1 or i < m - 1 and horizontalCut[i] > verticalCut[j]:
                ans += horizontalCut[i]* cntV
                i += 1
                cntH += 1
            else:
                ans += verticalCut[j] * cntH
                j += 1
                cntV += 1
        return ans
    def minimumCost2(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
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