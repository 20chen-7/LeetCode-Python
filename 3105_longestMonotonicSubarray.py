'''
find the peak and bottom outer loop, inner loop increment
'''
def longestMonotonicSubarray(a):
    ans = 1
    n = len(a)
    i = 0
    while i < n - 1:
        if a[i+1] == a[i]:
            i += 1
            continue
        i0 = 1
        inc = a[i+1] > a[i] # so here only > or <
        i += 2
        #main same pattern, increase or decrease , a[i] > a[i-1]  == inc
        while i < n and a[i] != a[i-1] and (a[i] > a[i-1]  == inc):
            i+= 1
        ans = max(ans, i-i0)#[i0,a-1] monotonic
        i -= 1 #boundary
    return ans
            