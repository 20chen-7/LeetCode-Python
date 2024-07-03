from math import isqrt, sqrt
#TC(O(min(sqrt(red), sqrt(blue)))

def maxHeightOfTriangle(red,blue):
    def f(m,n):
        i = 1
        left = [n, m]
        while left[i%2]>=i:
            left[i%2]-=i
            i+= 1
        return i - 1
    return max(f(red,blue), f(blue,red))
#TC(O(1))
def maxHeightOfTriangle2(red,blue):
    def f(m, n): 
        odd = isqrt(n)
        even = int((sqrt(4*m+1)/2-1))
        return 2*even +1 if even < odd else 2*odd
    return max(f(blue,red), f(red, blue))        