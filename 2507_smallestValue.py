def smallestValue(n):
    '''
    a + n/a <= n
    TC: O(sqrt(n))
    '''
    while True:
        x = n
        s = 0
        i = 2
        while i*i <= n:
            while x%i == 0:#i must be prime num
                s+= i
                x//=i
            i += 1
        if x > 1:
            s += x
        if s == n:
            return n
        n = s
        
        