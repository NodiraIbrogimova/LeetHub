class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s, hash_t = dict(), dict()
        for i in range(len(s)):
            if hash_s.get(s[i]) and hash_s[s[i]] != t[i]:
                return False
            hash_s[s[i]] = t[i]
            
        for i in range(len(t)):
            if hash_t.get(t[i]) and hash_t[t[i]] != s[i]:
                return False
            hash_t[t[i]] = s[i]
        
        return True
        
        
        
        # Approach 5:
        # Works if inputs are all English letters
        '''s_map, t_map = [None]*26, [None]*26
        a = ord('a')
        for i in range(len(s)):
            prehash = ord(s[i].lower()) - a
            # hash
            if s_map[prehash] is None:
                s_map[prehash] = t[i]
            elif s_map[prehash] != t[i]:
                return False
            
        for i in range(len(t)):
            prehash = ord(t[i].lower()) - a
            if t_map[prehash] is None:
                t_map[prehash] = s[i]
            elif t_map[prehash] != s[i]:
                return False
            
        for i in range(len(s)):
            key = ord(s[i].lower()) - a
            value = ord(s_map[key]) - a
            if s[i] != t_map[value]:
                return False
        return True
        '''
        
        # Approach 4
        # Create 2 hashmaps for strings
        # compare in 3rd pass, return decision
        mapping_s, mapping_t = {}, {}
        for i in range(len(s)):
            if s[i] not in mapping_s:
                mapping_s[s[i]] = t[i]
            elif mapping_s[s[i]] != t[i]:
                    return False
        # print('mapping s: ', mapping_s)
        for i in range(len(t)):
            if t[i] not in mapping_t:
                mapping_t[t[i]] = s[i]
            elif mapping_t[t[i]] != s[i]:
                    return False
        # print('mapping t: ', mapping_t)
        for val in mapping_s:
            # print('val and mappings: ', val, mapping_s[val], mapping_t.get(mapping_s[val]))
            if val != mapping_t.get(mapping_s[val]):
                return False
        return True
                
        
        '''
        Approach 3:
        Use set for value already assigned for s hashmap from t
        '''
        aset = set()
        hashmap = dict()
        for i in range(len(s)):
            if hashmap.get(s[i]) == None:
                if t[i] in aset:
                    return False
                hashmap[s[i]] = t[i]
                aset.add(t[i])
            elif hashmap[s[i]] != t[i]:
                return False
        return True
        
        '''
        Approach 2:
        Similar to approach 1, but using in-place transformation  for s and t
        Time complexity: O(n)
        Space complexity: O(1) -> as hashmap of chars is constant space
        '''
        s = self.transform2(s)
        t = self.transform2(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
        
        '''
        Approach 1: 
        Transform s and t to an array of digits
            Use a hashmap
            If char is in hashmap, it meant the char has already occured and we use the first occurance index as a digit for transformation
            Else, ude the current digit for transformed number version of the curr char
        Time complexity: O(n)
        Space complexity: O(n) -> for the array: result
        '''
        transform_s = self.transform(s)
        transform_t = self.transform(t)
        
        for i in range(len(transform_s)):
            if transform_s[i] != transform_t[i]:
                return False
        return True

    def transform2(self, astr):
        hashmap = dict()
        astr = list(astr)
        i = 0
        numericVal = 0
        while i < len(astr):
            if hashmap.get(astr[i]) == None:
                hashmap[astr[i]] = numericVal
                numericVal += 1
            astr[i] = hashmap[astr[i]]
            i += 1
        return astr
    
    def transform(self, astr):
        hashmap = dict()
        result = [0]*len(astr)
        i = 0
        while i < len(astr):
            if hashmap.get(astr[i]) == None:
                hashmap[astr[i]] = i
            result[i] = hashmap[astr[i]]
            i += 1
        return result

 