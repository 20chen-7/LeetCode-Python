# how to write recursion
- treat as recursion
    - current operation: pick or not pick
    - sub-problem: previous ith, max, min
    - next sub-problem: classify:
        - pick: previous (i-2)th max, min
        - not pick: previous (i-1)th max, min

# memorization search
- improve the memory
- save previous backtrack answer

## top-bottom: memorization search
## bottom-top: recurision

# 1:1 translate to recursion

- dfs -> f array
- recursion -> loop
- recursion boundary -> intials of array