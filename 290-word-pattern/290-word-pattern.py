class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        # edge case:
        if len(s) != len(pattern):
            return False
        
        # Approach 2
        # Record the occured strings
        # Once the recorded has been found again, check is pattern matches
        # return if no match is found
        occured = set()
        patterns = {}
        for i in range(len(pattern)):
            if not patterns.get(pattern[i]):
                if s[i] in occured:
                    return False
                patterns[pattern[i]] = s[i]
                occured.add(s[i])
            elif patterns[pattern[i]] != s[i]:
                return False
            patterns[pattern[i]] = s[i]
        return True
        
        # Approach 1
        # hashmap for char as a key and s as a value
        
        strs = {}
        for i in range(len(pattern)):
            if not patterns.get(pattern[i]):
                patterns[pattern[i]] = s[i]
                
            elif patterns[pattern[i]] != s[i]:
                return False
            
        for i in range(len(s)):
            if not strs.get(s[i]):
                strs[s[i]] = pattern[i]
            elif strs[s[i]] != pattern[i]:
                return False
            
        return True