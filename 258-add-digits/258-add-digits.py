class Solution:
    # asum = 0
    def addDigits(self, num: int) -> int:
        # Approach 3
        # Recursive approach: divide num and sum until num becomes < 10
        # base case: if the given val becomes less than 10, return value
        '''
        base case: when val < 1
        recursive case: 
        Keep adding digits until asum becomes < 10
        '''
        asum = 0
        while num > 0:
            asum += num % 10
            num //= 10
        if asum < 10:
            return asum
        return self.addDigits(asum)
        
        
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