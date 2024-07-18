from typing import List
'''
rob nums[0] or not:
    similar to rob1
'''

def rob1(self, nums: List[int]) -> int:
    f0 = f1 = 0
    for i, x in enumerate(nums):
        new_f = max(f0+x, f1)
        f0 = f1
        f1 = new_f
    return f1
def rob(self, nums: List[int]) -> int:
    return max(nums[0]+rob1(nums[2:-1]), rob(nums[1:]))
