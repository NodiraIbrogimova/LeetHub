class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # using KMP algorithm
        # find exact period of a string
        k = 0
        pi = [0]*len(s)
        
        for i in range(1, len(s)):
            k  = pi[i-1]
            
            while (k > 0) and (s[i] != s[k]):
                k = pi[k-1]
            if s[i] == s[k]:
                k += 1
            
            pi[i] = k
        return pi[-1] != 0 and len(s) % (len(s) - pi[-1]) == 0