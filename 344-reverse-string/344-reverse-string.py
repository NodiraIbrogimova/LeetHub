class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Approach 3
        # Time: O(n)
        # Space: O(1)
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]
            
        # Approach 2
        # Recursion
        # l = len(s)
        # if l < 2:
        #     return s
        # return self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])
        
        # Approach 1
        # Two pointers
        # Time: O(n)
        # Space: O(1)
        # left, right = (0, len(s)-1)
        # while left < right:
        #     temp = s[left]
        #     s[left] = s[right]
        #     s[right] = temp
        #     left += 1
        #     right -= 1
        