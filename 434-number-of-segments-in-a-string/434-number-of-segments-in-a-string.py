class Solution:
    def countSegments(self, s: str) -> int:
        # how to identify segment? 
        # segment - a piece in between space(s) if there's a space
        # new segment starts after a space
        # Time: O(n)
        # Space: O(1)
        
        space = chr(32)
        segment_count = 0
        i, j = 0, len(s)-1
        
        # pointers for a starting point of chars in string
        while i <= j and s[i] == space:
            i += 1
        
        while j > i and s[j] == space:
            j -= 1
            
        while (i <= j):
            if (i == 0 or s[i-1] == space) and s[i] != space:
                segment_count += 1
            i += 1    
        
        return segment_count