from functools import cache
from typing import List


def jewelleryValue(self, frame: List[List[int]]) -> int:
    def dfs(i, j):
        if i < 0 or j < 0:
            return 0
        return max(dfs(i-1,j), dfs(i, j-1)) + frame[i][j]
    return dfs(len(frame)-1, len(frame[0])-1)
'''
the logic correct, but TC & SC too large 
dfs(3,3) ---> finally dfs(2,2) 
memoriation search
initial memo, grid[i][j] > 0, so initiall val = 0
'''
def jewelleryValue2(self, frame: List[List[int]]) -> int:
    @cache
    def dfs(i, j):
        if i < 0 or j < 0:
            return 0
        return max(dfs(i-1,j), dfs(i, j-1)) + frame[i][j]
    return dfs(len(frame)-1, len(frame[0])-1)
'''
dfs => f array
recursive => loop
boundary => initial of f
f[i][j] = max(dfs(i, j-1) + grid[i][j], dfs(i-1, j) + grid[i][j])
if i = 0 or j = 0, out of boundary, add another row and col
f[i+1][j+1] = max(dfs(i, j+1) + grid[i][j], dfs(i, j+1) + grid[i][j])
f[i][0] = 0 f[0][j] = 0

TC:O(mn)
SC:O(mn)
'''
def jewelleryValue3(self, frame: List[List[int]]) -> int:
    m, n = len(frame), len(frame[0])
    f = [[0] * (n+1) for _ in range(m+1)]
    for i, row in enumerate(len(frame)):
        for j, x in enumerate(row):
            f[i+1][j+1] = max(f[i][j+1], f[i+1][j])+x
    return f[m][n]

'''
f[i+1] -> f[i], f[i-1] before unnecessary
so, using n+1
TC: O(mn)
SC: O(n)
'''
def jewelleryValue4(self, frame: List[List[int]]) -> int:
    m, n = len(frame), len(frame[0])
    f = [[0] * (n+1) for _ in range(2)]
    for i, row in enumerate(len(frame)):
        for j, x in enumerate(row):
            f[(i+1)%2][j] = max(f[i%2][j+1], f[(i+1)%2][j])+x
    return f[m%2][n]

'''
f[1][1] -> f[0][1],  f[1][2] -> f[0][1], f[0][2]
TC: O(mn)
SC: O(n)
'''

def jewelleryValue5(self, frame: List[List[int]]) -> int:
    m, n = len(frame), len(frame[0])
    f = [0]*(n+1)
    for row in frame:
        for j, x in enumerate(row):
            f[j+1] = max(f[j], f[j+1])+x
    return f[n]

'''
change original matrix
change frame[0]
f[i][j] = max(f[i-1][j], f[i],[j-1])+grid[i][j]
i = 0, f[j] = f[j-1]+grid[0][j] = f[j-1]+f[j]
j = 0, f[0] = f[0]+grid[i][0]
TC: O(mn)
SC: O(1)
'''

def jewelleryValue6(self, frame: List[List[int]]) -> int:
    m, n = len(frame), len(frame[0])
    f = frame[0]
    for j in range(1, n):
        f[j] += f[j-1]
    for i in range(1, m):
        f[0] += frame[i][0]
        for j in range(1, n):
            f[j] = max(f[j-1], f[j]) + frame[i][j]
    return f[-1]