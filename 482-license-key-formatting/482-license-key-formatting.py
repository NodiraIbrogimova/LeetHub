from collections import deque
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # n+1 groups with n dashes
        # for the algorithm use backward iteration
        result = deque([])
        i = len(s)-1
        while i >= 0:
            if s[i] != '-':
                if len(result) % (k+1) == k:
                    result.appendleft('-')
                result.appendleft(s[i].upper())
            i -= 1
        return "".join(result)