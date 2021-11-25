class Solution:
    def numberOfMatches(self, n: int) -> int:
        # Approach 2
        # For the example of n = 126, total of 125 matches are played
        # That's total of n-1 matches are played until one team is left
        # More examples can be checked with different [n]s
        return n-1
        
        # Approach 1
        # Check for odd and even type of integer, update the match and advances
        # Time: O(n)
        # Space: O(1)
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
            
            
        
        