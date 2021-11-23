class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches, advances = 0, 0
        while n > 1:
            match = n//2
            if n % 2:
                match -= 1/2
                matches += match
                advances += (match + 1/2)
                n -= match
            else:
                matches += match
                advances += match
                n -= match
        return int(matches)
            
            
        
        