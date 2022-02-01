class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Approach 1 (Nov 10th, 2021)
        # Time: O(n)
        # Space = O(1)
        prev = 0
        anext = 1
        maxProfit = -2**32-1
        while anext < len(prices):
            profit = prices[anext] - prices[prev]
            if profit < 0:
                # reset the buy date
                prev = anext
            else:
                if profit > maxProfit:
                    maxProfit = profit
            anext += 1
        return max(maxProfit, 0)
                
        # Approach (older version)
        
        if len(prices) == 0:
            return 0
        bought_trans = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] - bought_trans > max_profit:
                max_profit = prices[i] - bought_trans
            
            if bought_trans > prices[i]:
                bought_trans = prices[i]
        return max_profit
            
            
                
                
            
        
        