###
- [Reference Links](https://leetcode.cn/problems/range-sum-query-2d-immutable/solutions/2667331/tu-jie-yi-zhang-tu-miao-dong-er-wei-qian-84qp/)

# How to initial 2D prefix Sum:

- Prefix[i+1][j+1] = Prefix[i+1][j] + Prefix[i][j+1] - Prefix[i][j] + a[i][j]

# How to get random sub matrix Sum:

- leftTopCorner: a[r1][c1]
- rightBottomCorner: a[r2][c2]
- Sum = Prefix[r2][c2] - Prefix[r1][c2] - Prefix[r2][c1] + Prefix[r1][c1]

# Leetcode
- [304](https://leetcode.cn/problems/range-sum-query-2d-immutable)
- [1277](https://leetcode.cn/problems/count-square-submatrices-with-all-ones/)
- [1504](https://leetcode.cn/problems/count-submatrices-with-all-ones/description/)
