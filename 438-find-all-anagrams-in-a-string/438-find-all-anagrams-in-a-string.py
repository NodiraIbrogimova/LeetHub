class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pHash = defaultdict(int)
        count = 0
        for char in p:
            pHash[char] += 1
        res = []
        rHash = defaultdict(int)
        
        for idx, char in enumerate(s):
            if idx >= len(p): # Deleting last idx to maintain sliding window
                letterToRemove = s[idx - len(p)]
                if rHash[letterToRemove] > 1:
                    rHash[letterToRemove] -= 1
                else:
                    del rHash[letterToRemove]
            rHash[char] += 1
            if pHash == rHash:
                res.append(idx - len(p) + 1) 
        return res
    
        # Approach 1
        # Brute-force
#         result = []
#         until = len(p)-1
#         start, end = 0, until
#         while end < len(s):
#             pattern = Counter(p)
#             head = start
#             if s[start] in pattern and s[end] in pattern:
#                 while start < end:
#                     if s[start] not in pattern or s[end] not in pattern or pattern[s[start]] <= 0 or pattern[s[end]] <= 0:
#                         break
#                     pattern[s[start]] -= 1
#                     pattern[s[end]] -= 1
#                     start += 1
#                     end -= 1
#                 else:
#                     if start == end:
#                         pattern[s[start]] -= 1
#                     allZero = True
#                     for val in pattern:
#                         if pattern[val] < 0:
#                             allZero = False
#                             break
#                     if allZero:
#                         result.append(head)
#             start  = head + 1
#             end = start + until
                
#         return result
                
        