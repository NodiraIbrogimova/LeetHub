class Solution:
    def reverseWords(self, s: str) -> str:
        alist = list(s)
        start, end = 0, 0
        i = 0
        while i < len(alist):
            if alist[i] == ' ':
                end = i - 1
                while start < end:
                    alist[start], alist[end] = alist[end], alist[start]
                    start += 1
                    end -= 1
                start = i + 1
            i += 1
        if start < i:
            end = i - 1
            while start < end:
                alist[start], alist[end] = alist[end], alist[start]
                start += 1
                end -= 1
        return "".join(alist)
        
        