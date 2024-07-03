'''
tree DP $12.1
diameter


1. one tree is super long, so the shortest will be the diameter of the tree d1/d2
2. d1 close to d2, D = [(d1+1)/2]+[(d2+1)/2]+1
so max(d1, d2, D)
TC O(n+m)
SC O(n+m)
'''
def diameter(edges):
    g = [[] for _ in range(len(edges)+1)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)
    res = 0
    def dfs(x, fa):
        nonlocal res
        maxL = 0
        for y in g[x]:
            if y != fa:
                subL = dfs(y,x)+1
                res = max(res,maxL+subL)
                maxL = max(maxL, subL)
        return maxL
    dfs(0,-1)
    return res
def minimumDiameterAfterMerge(edges1, edges2):
    d1 = diameter(edges1)
    d2 = diameter(edges2)
    return max(d1, d2, (d1+1)//2+(d2+1)//2+1)