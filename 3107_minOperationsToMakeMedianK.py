'''
sort first, find smaller than k,and larger than k
[2,5,6,8,5] k = 4 return 2
[2,5,6,8,5] k = 7 return 3
'''

from bisect import bisect_left
from itertools import accumulate


def minOperationsToMakeMedianK(nums, k):
    nums.sort()#O(nlogn), or can choose quickselect, if wanna median val
    m = len(nums)//2
    ans = 0
    if nums[m] > k:
        for i in range(m, -1, -1):
            if nums[i] <= k:
                break
            ans += nums[i] - k
    else:
        for i in range(m, len(nums)):
            if nums[i] >= k:
                break
            ans += k - nums[i]
    return ans
def minOperationsToMakeMedianK2(nums, k):
    n = len(nums)
    nums.sort()#O(nlogn), or can choose quickselect, if wanna median val
    m = n//2
    idx = bisect_left(nums, k)
    prefix = list(accumulate(nums, initial=0))
    if idx <= m:
        return prefix[m+1]-prefix[idx]-k*(m+1-idx)
    else:
        return k*(idx-m)-(prefix[idx]-prefix[m])

'''
if more inputs queries[]
give more k, queries[4,7], return ans[2,3]
2, [5,5], 6,8
[5,5] >=k= 4, prefix -...
'''
def minOperationsToMakeMedianKs(nums, queries):
    n = len(nums)
    nums.sort()#O(nlogn), or can choose quickselect, if wanna median val
    m = n//2
    prefix = list(accumulate(nums, initial=0))
    ans = []
    for k in queries:
        idx = bisect_left(nums, k)
        if idx <= m:
            ans.append(prefix[m+1]-prefix[idx]-k*(m+1-idx))
        else:
            ans.append(k*(idx-m)-(prefix[idx]-prefix[m]))
    return ans
print(minOperationsToMakeMedianKs([2,5,6,8,5], [4,7]))#[2,3]