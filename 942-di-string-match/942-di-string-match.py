class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        amin, amax, i = 0, len(s), 0
        perm = [0]*(amax+1)
        while i < len(perm)-1:
            if s[i] == 'I':
                perm[i] = amin
                amin += 1
            else:
                perm[i] = amax
                amax -= 1
            i += 1
        perm[i] = amin
        return perm
        
        