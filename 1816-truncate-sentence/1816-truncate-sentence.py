class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s + ' '
        i = 0
        while i < len(s) and k > 0:
            if s[i] == chr(32):
                k -= 1
            i += 1
        return s[:i-1]