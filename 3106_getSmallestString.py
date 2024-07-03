'''
k = 0, return s
if k = 1, s[0] != 'a', change s[0], so greedy algorithm
every time, change 1, and k times, s[i]+1 or -1
'''
def getSmallestString(s, k):
    s = list(s)
    for i, c in enumerate(map(ord,s)):
        dis = min(c-ord('a'), ord('z') + 1 - c)
        if dis > k:
            s[i] = chr(c-k)
            break
        k -= dis
        s[i] = 'a'
    return ''.join(s)