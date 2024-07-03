'''
or , bit manipulation, more and less
-1 -> 1111111, -1 --> (~1)+1 ==> -1 & x = x
0-1-3,  4    0-1 => 7, 1-3 =>7, 1-2=>1, 4
  |
  2
so ids          cc_and
    0->0        0->1  (7&7&1=1)
    1->0
    2->0
    3->0
    4->1        1->-1, ISOLATED
    
TC: O(n+m+q), m=len(edges) q=len(query)
SC: O(n+m)
    DFS
'''
def minimumCost(n, edges, queries):
    g = [[] for _ in range(n)]
    for x, y, w in edges:
        g[x].append((y, w))
        g[y].append((x, w))
    def dfs(x):
        and_ = -1
        ids[x] = len(cc_and)
        for y, w in g[x]:
            and_ &= w
            if ids[y] < 0:
                and_ &= dfs(y)
        return and_
    ids = [-1]*n
    cc_and = []
    for i in range(n):
        if ids[i] < 0:
            cc_and.append(dfs(i))
    return [0 if s == t else -1 if ids[s]!=ids[t] else cc_and[ids[s]] for s, t in queries]
            
'''
x&x = x, x&y <= min(x,y)
union find
s /= t, s connected w/ t, nonnegative
s = t, do not move, so zero
s, t isolationed, -1
'''
def minimumCost2(n, edges, queries):
    fa = list(range(n))
    and_ = [-1]*n
    def find(x):
        if fa[x]!=x:
            fa[x] = find(fa[x])
        return fa[x]
    for x, y, w in edges:
        x = find(x)
        y = find(y)
        and_[y] &= w
        if x != y:
            and_[y] &= and_[x]
            fa[x] = y
    return [-1 if find(s)!=find(t)else and_[find(s)] for s, t in queries]