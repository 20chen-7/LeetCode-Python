class Solution:
    '''
    my
    '''
    def getSmallestString(self, s: str) -> str:
        listS = list(s)
        prev = int(s[0])
        for i, c in enumerate(s):
            if i == 0:
                continue
            if int(c)%2 == prev%2 and int(c) < prev:
                listS[i], listS[i-1] = str(prev), c
                break
            prev = int(c)
        return ''.join(listS)
    
    def getSmallestString2(self, s: str) -> str:
        t = list(s)
        for i in range(1, len(t)):
            x, y = t[i-1], t[i]
            if x > y and ord(x)%2 == ord(y)%2:
                t[i-1], t[i] = t[i], t[i-1]
                break
        return ''.join(t)
    

