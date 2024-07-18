from string import ascii_lowercase
from typing import List


def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        '''
        dp[0] = 0 
        dp[i] = max(dp[i-1],dp[i-1]+(ord(c)-ord('a')), dp[i-1]+vals[idx])
        '''
        t = list(chars)
        dp = [0]*(len(s)+1)
        for i in range(1, len(s)+1):
            curr = ord(s[i-1])-ord('a') + 1
            if s[i-1] in t:
                curr = vals[t.index(s[i-1])]
            dp[i] = max(dp[i-1]+curr, curr)
        return max(dp)

def maximumCostSubstring2(self, s: str, chars: str, vals: List[int]) -> int:
        '''
        O(n+|len ascii|)
        O(|len ascii|)
        '''
        mapping = dict(zip(ascii_lowercase, range(1, 27)))|dict(zip(chars, vals))
        f = 0
        ans = 0
        for c in s:
            f = max(f, 0)+mapping[c]
            ans = max(f, ans)
        return ans
                