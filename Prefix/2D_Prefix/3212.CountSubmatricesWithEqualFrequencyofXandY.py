'''
[0,0] -> [i,j] sub-matrix #x==#y
prefix
x,y,.
y,.,.

(1,0), (0,1),(0,0)
(1,1), (0,1), (0,0)
prefix
second row prefix 
first mean #x and second mean #y

TC:O(mn) 
SC:O(n)

'''


def numberOfSubmatrices(grid):
    ans = 0
    cols_cnt = [[0,0] for _ in range(grid[0])]
    for row in range(len(grid)):
        s0 = s1 = 0
        for j, c in enumerate(grid[row]):
            # if c == "x":
            #     cols_cnt[j][0] += 1
            # elif c == "y":
            #     cols_cnt[j][1] += 1
            if c != ".":
                cols_cnt[j][ord(c)&1] += 1
            s0 += cols_cnt[j][0]
            s1 += cols_cnt[j][1]
            if s0>0 and s1 == s0:
                ans += 1
    return ans