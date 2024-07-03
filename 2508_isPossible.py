'''
max <= 2 edges
degree for each V is 2

one E will change two nodes, each node has odd degree, so totally, 
there are 0, 2, 4 nodes w/ odd degree, three situations

odds = [], m = len(odds)
m = 0, return True
m = 2, two nodes(A,B) wo edge, if w/ edge,  find another node C w/ even edges, AC, BC(require enumerations)
m = 4, (A, B, C, D), [AB, CD],[AC, BD],[AD, BC]

in order to fast check connected or not, using HashTable
'''
from collections import defaultdict, Counter
def isPossible(n, edges):
    g = defaultdict(set)
    deg = Counter()
    for x, y in edges:
        g[x].add(y)
        g[y].add(x)
        deg[x] += 1
        deg[y] += 1
    odd = [i for i, d in deg.items() if d%2]
    m = len(odd)
    if m == 0: return True
    if m == 2:
        x, y = odd
        if x not in g[y]:
            return True
        for i in range(1, n+1):
            if i!= x and i!=y and x not in g[i] and y not in g[i]:
                return True
        return False
    if m == 4:
        a, b, c , d = odd
        return  b not in g[a] and d not in g[c] or \
                c not in g[a] and d not in g[b] or \
                d not in g[a] and c not in g[b] 
    return False
            
        
    