from collections import Counter
def similarPairs(words) -> int:
    dct = Counter()
    ans = 0
    for word in words:
        mask = 0
        for c in word:
            mask |= 1<<ord(c)-ord('a')
        ans += dct[mask]  #so the similar not the same, the last digit not same
        dct[mask] += 1
    return ans