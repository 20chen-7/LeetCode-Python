def rob(nums) -> int:
    n = len(nums)
    cache = [-1]*n
    def dfs(i):
        if i < 0:
            return 0
        if cache[i] != -1:
            return cache[i]
        res = max(dfs(i-1), dfs(i-2)+nums[i])
        cache[i] = res
        return res
    return dfs(n-1)
'''
TC: O(n)
SC: O(n)
'''
def rob2(nums) -> int:
    n = len(nums)
    f = [0]*(n+2)
    for i, x in enumerate(nums):
        f[i+2] = max(f[i+1], f[i]+x)
    return f[n+1]

'''
TC: O(n)
SC: O(1)
'''
def rob3(nums) -> int:
    n = len(nums)
    f0 = f1 = 0
    for i, x in enumerate(nums):
        new_f = max(f1, f0+x)
        f0 = f1
        f1 = new_f
    return f1