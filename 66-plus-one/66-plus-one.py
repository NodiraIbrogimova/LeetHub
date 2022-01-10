class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # warm-up
        i = len(digits)-1
        carry = 0
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i -= 1
        return [1] + digits
        
        
        
        
        
        
        '''
        Approach 3:
        1 - Loop through the array
        2 - Check for the edge case: when digit is 9
            if digit is less than 9, we can inc it and return the digits
            else we need to keep updating that digit to 0 and at the end return [1] pushed to the start of the array as the size of the digits would increase for inc by 1 if each digit would be 9
        '''
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i -= 1
        return [1] + digits
        
        '''
        Approach 2: 
        Change the digits list in-place
        
        Time complexity: O(n)
        Space complexity: O(1)
        '''
        # remainder = 1
        # i = len(digits) - 1
        # while i >= 0:
        #     result = digits[i] + remainder
        #     digits[i] = result % 10
        #     remainder = result // 10
        #     i -= 1
        # if remainder:
        #     return [remainder] + digits
        # return digits
    
    
        '''
        Approach 1: 
        Using new array for storing result and reading digits from the end of digits list
        
        Time complexity: O(n)
        Space complexity: O(n)
        '''
#         remainder = 1
#         arr = [0] * len(digits)
#         i = len(digits) - 1
        
#         while i >= 0:
            
#             result = digits[i] + remainder
#             arr[i] = result % 10
#             remainder = result // 10
#             i -= 1
#         if remainder:
#             arr = [remainder] + arr
#         return arr
        