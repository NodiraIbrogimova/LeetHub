class Solution:
    def longestPrefix(self, s: str) -> str:
        pi = [0]*len(s)
        for i in range(1, len(s)):
            k = pi[i-1]
            
            while k > 0 and s[i] != s[k]:
                k = pi[k-1]
            if s[i] == s[k]:
                k += 1
            pi[i] = k
        print('pi is: ', pi)
        return s[len(s)-pi[-1]:]
        
        
        # i, j = 1, 0
        # table = [0]
        # while i < len(s):
        #     while j and s[i] != s[j]:
        #         j = table[j-1]
        #     if s[i] == s[j]:
        #         j += 1
        #         table.append(j+1)
        #     else:
        #         table.append(0)
        #         j = 0
        #     i += 1
        # print('table: ', table)
        # return s[len(s) - table[-1]]
        