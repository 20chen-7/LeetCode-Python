
'''
DP also work
m-1 down, n-1 right
totally m+n-2 chose m-1 down, n-1 right
/frac{(m+n-2)!}{(m-1)}
TC: O(m)
SC: O(1)
'''
from math import comb


def uniquePaths(self, m: int, n: int) -> int:
    return comb(m+n-2, n-1)