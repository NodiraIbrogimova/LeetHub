class Solution:
    def isPalindrome(self, x: int) -> bool:
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