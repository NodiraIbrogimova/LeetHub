class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == turnedOn]
        if turnedOn > 8:
            return []
        result = []
        
        def dfs(self, turnedOn):
            if turnedOn <= 0:
                return
            
        
        self.dfs(turnedOn)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # return ['%d:%02d' % (h, m)
        #     for h in range(12) for m in range(60)
        #     if (bin(h) + bin(m)).count('1') == num]
        