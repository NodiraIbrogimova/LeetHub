class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) < len(s):
            return ""
        if len(s) == 0:
            return t
        xor = ord(s[0]) ^ ord(t[0])
        for i in range(1, len(s)):
            xor ^= ord(t[i])
            xor ^= ord(s[i])
        xor ^= ord(t[-1])
        return chr(xor)