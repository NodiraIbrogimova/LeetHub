class Solution:
    def longestPalindrome(self, s: str) -> int:
        aset = set()
        for achar in s:
            if achar in aset:
                aset.remove(achar)
            else:
                aset.add(achar)
        return len(s) - len(aset) + (1 if len(aset) > 0 else 0) 