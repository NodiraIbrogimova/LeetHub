class Solution:
    def romanToInt(self, s: str) -> int:
        # Warm-up
        '''
        There are two cases:
        1. when previous number is I, X and we have to iterate until 
        this ends or reachs number which is available with another roman number
        example:
        VIII = 5 + 3
        IIII -> can be written as IV
        2. When number to the left is smaller and we have to subtract it
        
        Hence, each time we have to add element 
        '''
        hashmap = {'I': 1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
        last = s[-1]
        output = 0
        for i in range(len(s)-1, -1, -1):
            curr = s[i]
            if hashmap[last] > hashmap[curr]:
                output -= hashmap[curr]
            else:
                output += hashmap[curr]
            last = curr
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += translations[char]
#         return number
        