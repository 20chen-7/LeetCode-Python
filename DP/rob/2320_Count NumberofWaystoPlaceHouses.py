MOD = 1_000_000_007
'''
ith, i placed, i-1 can't f[i] = f[i-2]
ith, i not placed, i-1 can placed, f[i] = f[i-1]
f[i] = f[i-1] + f[i-2]
single side, f[n], two side, f[n]*f[n]
every time, Fibonacci num
'''
f = [1, 2]

for _ in range(1_000_0-1):
    f.append((f[-1]+f[-2])%MOD)

def countHousePlacements(self, n: int) -> int:
    return (f[n]**2)%MOD
    