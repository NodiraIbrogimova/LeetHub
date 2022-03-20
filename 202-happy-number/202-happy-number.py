class Solution:
    def isHappy(self, n: int) -> bool:
        # Approach 4: With recursion
        memoized = set()
        def checkHashmap(n):
            if n == 1:
                return True
            if n in memoized:
                return False
            asum = 0
            memoized.add(n)
            while n > 0:
                asum += (n%10)**2
                n //= 10
            return checkHashmap(asum)
        return checkHashmap(n)

    
        # Approach 3:
        # Alternative way of solving with hardcoding
        # This approach was based on the idea that all numbers either end at 1 or enter the cycle {4, 16, 37, 58, 89, 145, 42, 20}, wrapping around it infinitely.
        # Taken from Solution part of the problem
        while n != 1 and n != 4:
            n = self.getNext(n)
        return n == 1
        
        
        # Approach 2:
        # Floyd's Cycle finding algorithm: one fast and one slow runners on getNext
        slow, fast = n, self.getNext(n)
        while fast != 1 and fast != slow:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))
        return fast == 1    
            
        # Approach 1:
        # First suggestion in Solution
        # Time: O(logn)
        # Space: O(logn)
        # Given a number n, what is its next number?
        # Follow a chain of numbers and detect if we've entered a cycle.
        seen = set()
        while (n != 1) and (n not in seen):
            next = self.getNext(n)
            seen.add(next)
        return n == 1
            
    def getNext(self, n: int):
        next = 0
        while n > 0:
            digit = n % 10
            next += digit*digit
            n //= 10
        return next