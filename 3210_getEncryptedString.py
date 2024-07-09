def getEncryptedString(s, k):
 k %= len(s)
 return s[k:]+ s[:k]