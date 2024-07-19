def uniquePaths(self, m: int, n: int) -> int:
        f = [[0]*(n) for _ in range(m)]
        for i in range(m):
            f[i][0] = 1
        for j in range(n):
            f[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                f[i][j] = f[i][j-1] + f[i-1][j]
        return f[-1][-1]
def uniquePaths2(self, m: int, n: int) -> int:
        f = [1]*m
        for j in range(1, n):
            for i in range(1, m):
                f[i] = f[i-1]+f[i]
        return f[-1]

            