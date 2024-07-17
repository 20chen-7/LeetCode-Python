# Two method
- f[i] represents the max sum of sub array ending with a[i], a.k.a Kadane Algorithm
    - not connecting with left side, f[i] = a[i]
    - connecting with left side, f[i] = f[i-1]+a[i]
    - Max Val => f[i] = max(f[i-1], 0)+a[i]
- Prefix Sum