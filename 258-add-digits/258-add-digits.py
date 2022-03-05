class Solution:
    # asum = 0
    def addDigits(self, num: int) -> int:
        # Approach 2
        # Iterative, brute-force
        # TC: O(n)
        # SC: O(n)
        asum = num
        # check if asum became a single digit number
        while asum > 9:
            num = asum
            asum = 0
            while num > 0:
                asum += (num % 10)
                num //= 10
        return asum
    
        # Approach 1
        # Iterative
        # asum = 0
        # if num // 10 <= 0:
        #     return num
        # curr = self.addDigits(num // 10)
        # asum += (curr % 10)
        # return asum
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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