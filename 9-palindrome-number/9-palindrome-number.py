class Solution:
    def isPalindrome(self, x: int) -> bool:
        # warm-up
        # TC: O(log10)
        # SC: O(1)
        if x < 0:
            return False
        opposite = 0
        value = x
        while x > 0:
            remainder = (x - x//10*10)
            opposite = opposite*10 + remainder
            x //= 10
        return opposite == value
        
        # Approach 2
        # Wrap to string and check with its opposite
        # very slow
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
    
        count = 0
        value = 0
        original = x
        while x > 0:
            value += (x%10)*(10**count)
            print('value is: ', value)
            x //= 10
            count += 1
        return value == original