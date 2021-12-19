class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Approach 2
        # Check only the tail of the string
        # Trim if empty space is present
        # iterate until the next space
        space = chr(32)
        i = len(s)-1
        count = 0
        while i>=0 and s[i] == space:
            i -= 1
        
        while i>=0 and s[i] != space:
            count += 1
            i -= 1
        return count
        
        
        
        # Approach 1:
        # Time complexity: O(n)
        # Space complexity: O(1)
        
        right = len(s)-1
        while right >= 0:
            if s[right] != chr(32):
                break
            right -= 1
        
        alen = 0
        while right >= 0 and s[right] != chr(32):
            alen += 1
            right -= 1
        return alen
            
            
                
        