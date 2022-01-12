class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # Warm-up
        start = 1
        total = duration
        prev = timeSeries[0] + duration - 1
        while start < len(timeSeries):
            if prev >= timeSeries[start]:
                total -= (prev - timeSeries[start] + 1)
            total += duration
            prev = timeSeries[start] + duration - 1
            start += 1
        return total 
                
            
            
            
            
            
        
        
        
        
        # Approach 1
#         i = 0
#         asum = 0
#         while i < len(timeSeries)-1:
#             expected_end = timeSeries[i] + duration - 1
#             next_shoot = timeSeries[i+1]

#             if next_shoot > expected_end:
#                 asum += duration
#             else:
#                 asum += (next_shoot - timeSeries[i])
#             i += 1
#         return asum + duration
        