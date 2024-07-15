from functools import cache
from typing import List

'''
The @cache decorator in Python, specifically from the functools module, is used to store the results of expensive function calls and return the cached result when the same inputs occur again. This technique is known as memoization. Here's why adding @cache to the dfs function within the combinationSum4 method is beneficial:

Avoid Re-computation: In the context of calculating the number of combinations that sum up to a target value, many subproblems are solved repeatedly. For example, when calculating combinations that sum up to 10 using numbers [1, 2, 3], you might need to calculate the combinations for 9, 8, and 7 multiple times. By caching these results, you avoid re-computation and significantly speed up the process.

Optimize Recursive Calls: The function dfs is recursive and explores each possible combination that sums up to the target. This can lead to an exponential number of possibilities. With memoization, once a subproblem (i.e., a smaller target value) is solved, its result is stored. Any subsequent need for this result can be fulfilled by a simple lookup rather than recalculating it.

Enhance Performance: The use of @cache converts a potentially exponential time complexity problem into a polynomial one. It ensures that each unique argument to the dfs function is processed exactly once, reducing the overall number of calls drastically.

Simplicity: Using the @cache decorator simplifies the code by abstracting the caching mechanism. You don't need to manually implement a storage structure to hold the results of previous computations. This reduces the chance of errors and improves code readability.


'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1, target+1):
            used = set()
            for j in range(len(nums)):
                if i - nums[j] >= 0:
                    dp[i] += dp[i-nums[j]]
        return dp[target]
    def combinationSum42(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(x):
            if x == 0:
                return 1
            return sum(dfs(x-num) for num in nums if x-num>=0)
        return dfs(target)