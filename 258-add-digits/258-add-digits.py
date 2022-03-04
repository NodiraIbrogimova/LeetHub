class Solution:
    def addDigits(self, num: int) -> int:
        # if num
#         if num // 10 <= 0:
#             return num
#         curr = addDigits()
#         asum += curr
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9
        asum = 0
        result = 0
        while num > 0:
            asum += num % 10
            result += asum % 10
            asum //= 10
            num //= 10
            
        # result = 0
        total = 0
        while result > 0:
            total += result % 10
            result //= 10
        return total