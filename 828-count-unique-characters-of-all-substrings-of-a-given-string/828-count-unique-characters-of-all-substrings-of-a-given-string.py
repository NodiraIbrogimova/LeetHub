class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        a = defaultdict(list)
        for i in range(n):
            a[s[i]].append(i)
        ans = 0
        for p in a.values():
            m = len(p)
            for i in range(m):
                l,r = 0,0
                if i==0: 
                    l = p[i] + 1
                else: 
                    l = p[i] - p[i-1]
                if i<m-1:
                    r = p[i+1] - p[i]
                else:
                    r = n - p[i]
                ans += l*r
        return ans
            
        