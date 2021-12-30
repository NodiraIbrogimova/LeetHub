class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        head = 0
        jump = 2*k
        while head < len(s):
            start, end = head, min(head + k-1, len(s)-1)
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            head += jump

        return ''.join(s)
        
        