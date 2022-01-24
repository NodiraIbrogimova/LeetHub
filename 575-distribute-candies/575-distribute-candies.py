class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        types = set()
        total = len(candyType)
        max_allowed = len(candyType)//2
        i = 0
        while i < total and len(types) <= max_allowed:
            types.add(candyType[i])
            i += 1
        return min(total//2, len(types))
        
        
        
        
        
        '''
        Approach 1:
        Use hashset to store all possible variants of candies
        Iterate through variants and check if iterations don't exceed the limit for cases:
            1. Hashset in smaller than n//2
            2. Hashset is bigger than n//2
        Inc count for each value seen in hashset
        
        Time complexity: O(n)
        Space complexity: O(n)
        '''
        hashset = set(candyType)
        return min(len(hashset), len(candyType)//2)