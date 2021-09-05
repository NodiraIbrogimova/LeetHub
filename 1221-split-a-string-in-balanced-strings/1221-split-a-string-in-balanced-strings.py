class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balancer = 0
        for achar in s:
            if achar == 'L':
                balancer += 1
            else:
                balancer -= 1
            
            if balancer == 0:
                count += 1
        return count