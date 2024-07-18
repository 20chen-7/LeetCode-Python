# Two method
- f[i] represents the max sum of sub array ending with a[i], a.k.a Kadane Algorithm
    - not connecting with left side, f[i] = a[i]
    - connecting with left side, f[i] = f[i-1]+a[i]
    - Max Val => f[i] = max(f[i-1], 0)+a[i]
- Prefix Sum

## Key Notes:
- mapping = dict(zip(ascii_lowercase, range(1, 27)))|dict(zip(chars, vals)), union of two, right will cover left

- Kadane's Algorithm(1191)
The max sum of subarray existed in single array, maxSum = #53
The max sum of subarray existed in two arrays, maxSum = maxPrefixSUM+maxPostfixSUM
The max sum of subarray existed in multiple arrays, maxSum = maxSingleArraySUM > 0, 
sum of (k-2) array + maxPrefixSUM+maxPostfixSUM