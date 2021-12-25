class Solution:
    def firstUniqChar(self, s: str) -> int:
        # warm-up
        # check the xor
        count = [0]*26
        a = ord('a')
        for achar in s:
            position = ord(achar) - a
            count[position] += 1
        for i in range(len(s)):
            position = ord(s[i]) - a
            if count[position] == 1:
                return i
        return -1
        
        
        # Time (two pass) = O(2*n) => O(n)
        # Space: O(1) for count for 26 chars
#         count = [2]*26
#         a = ord('a')
#         # Approach (solving hash table card)
#         # Optimization of the 2nd Approach
#         for achar in s:
#             position = ord(achar) - a
#             count[position]  = (count[position] >> 1)
#         for i in range(len(s)):
#             position = ord(s[i]) - a
#             if count[position] & 0b00000001:
#                 return i
#         return -1
            
#         # Approach 2:
#         # Using count array of chars[26]
#         # Time: O(n)
#         # Space: O(1)
#         count = [0]*26        
#         a = ord('a')
#         for achar in s:
#             count[ord(achar) - a ] += 1
#         for i in range(len(s)):
#             if count[ord(s[i])-a] == 1:
#                 return i
#         return -1
        
#         # Approach 1
#         # Count the freq of each char in string
#         # Iterate through the dictionary and dec the freq of each met char
#         # return the one with 0 freq
#         hashmap = dict()
#         for achar in s:
#             hashmap[achar] = hashmap.get(achar, 0) + 1
        
#         for i in range(len(s)):
#             if hashmap[s[i]] == 1:
#                 return i
#         return -1