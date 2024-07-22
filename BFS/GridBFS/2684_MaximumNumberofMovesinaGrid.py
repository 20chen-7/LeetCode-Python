from typing import List
'''
bfs, visited => 0
TC: O(mn)
SC: O(n)
dfs also work
'''

def maxMoves(self, grid: List[List[int]]) -> int:

    m, n = len(grid), len(grid[0])
    vistited = [-1]*m
    q = range(m)
    for j in range(n-1):
        tmp = q
        q = []
        for i in tmp:
            for k in i-1, i, i+1:
                if 0<=k<m and vistited[k]!=j and grid[k][j+1]>grid[i][j]:
                    vistited[k] = j
                    q.append(k)
        if not q:
            return j
    return n-1
'''
TC: O(mn)
SC: O(1)
'''
def maxMoves2(self, grid: List[List[int]]) -> int:

    m, n = len(grid), len(grid[0])
    for row in grid:
        row[0] *= -1
        
    for j in range(n-1):
        for i, row in enumerate(grid):
            if row[j] > 0:
                continue
            for k in i-1, i, i+1:
                if 0<=k<m and grid[k][j+1]>-row[j]:
                    grid[k][j+1]*=-1
                    
        if all(row[j+1] > 0 for row in grid):
            return j
    return n-1

