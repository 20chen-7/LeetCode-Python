def cycleLengthQueries(n, queries):
    '''
    2^n-1 node complete binary tree, left Node-> 2*val, right Node 2*val+1,
    queris = [ai,bi], connected
    Longtest common ancestor(LCA), dist(LCA,ai)+dist(LCA, bi)+1
    each time chose deeper(bigger) node and move up, reduce repeating paths.
       1
     2,  3
    4,5 6,7 , 5<->3
    TC(nq)
    '''
    for i, (a, b) in enumerate(queries):
        res = 1
        while a!= b:
            if a > b: a//=2
            else: b//=2
            res += 1
        queries[i] = res
    return queries
'''

from bit manpulation, left node x.bit_length() + 0, right node x.bit_length() + 1
LCA , find longest common prefix for two bit 
a is the samller number, so  d = b.bit_length() - a.bit_length()>0
then b>>d, so b move up to the same level with a
a^b, if a^b == 0, mean a, b are the LCA, else, a and b move up a^b value to LCA

TC(q)
'''
def cycleLengthQueries2(n, queries):
    for i, (a, b) in enumerate(queries):
        if a > b: a, b = b, a
        d = b.bit_length() - a.bit_length()
        queries[i] = d+(a^(b>>d)).bit_length()*2+1
    return queries
    
print(cycleLengthQueries2(3, [[5,3],[4,7],[2,3]]))#[4,5,3]