'''
How to determine adjacent zeros Binary, 
x = ~i
1001
0110

then x>>1
0110 ^
0011
so two adjacent & == 0, no adjacent zeros
'''
def validStrings(n):
    mask = (1<<n)-1# all '1'
    ans = []
    #O(x^n)
    for i in range(1<<n):
        x = mask^i # get all 1 binary with length n
        if (x&(x>>1)) == 0:
            #O(n)
            ans.append(f"{i:0{n}b}") #i => change to length n,filling 0 binary
            '''
            0: This means that the number should be padded with zeros if it is shorter than the specified width.
            {n}: This specifies the width of the output, which is determined by the value of n. Since this is inside curly braces, it will be replaced with the value of the variable n at runtime.
            b: This indicates that the number should be formatted as a binary number.
            '''
    return ans

'''
the results can be Fibonacci number, so 1.68^n
so totally O(2^n+n*1.68^n)=> O(2^n)
'''


        