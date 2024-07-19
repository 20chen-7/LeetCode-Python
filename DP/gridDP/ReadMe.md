# Find Sub problems
- dfs(i, j) presents from left top corner to ith row, jth col
- dfs(i, j): 
    - dfs(i, j-1) + grid[i][j] from left side
    - dfs(i-1, j) + grid[i][j] from top side
    - max
- boundary condition:
    - i < 0 or j < 0, return 0
- recursion:
    - dfs(m-1, n-1)

