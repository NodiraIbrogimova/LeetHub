class Solution:
    def isAlphaNumeric(self, value):
        return (ord('A') <= ord(value) <= ord('Z')) or (ord('a') <= ord(value) <= ord('z')) or (ord('0') <= ord(value) <= ord('9'))
    
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:	
            # iterate left and right until char in  [48:57], [65,90], [97:122] ranges met
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        
        
        
        '''
        What are the characteristics of a palindrome?
        1. Check if a value is alphanumeric for both left and right pointers.
            Iterate through until both left and right are alphanumeric values
        2. Convert found alphanumeric values to lower to check if they are equal
            Directly return False once not equal has been found
        '''
        left, right = 0, len(s)-1
        
        while left < right:
            
            while left < right and not self.isAlphaNumeric(s[left]):
                left += 1
            
            while right > left and not self.isAlphaNumeric(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True
        
        