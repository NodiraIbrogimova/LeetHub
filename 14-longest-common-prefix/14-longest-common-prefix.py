class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        
        # Warm-up in pair coding with Uulzhan
        shortestElement = min(strs, key=len)
        longestPrefix = len(shortestElement)-1
        for i in range(len(strs)):
            high = longestPrefix
            curr_el = strs[i]
            while high >= 0:
                if curr_el[high] != shortestElement[high]:
                    longestPrefix = high - 1
                high -= 1
            if longestPrefix < 0:
                return ""
        return shortestElement[:longestPrefix+1]
        
        
        
        # Approach 2
        # find the shortest string and use it for comparison from tail to head for each other string
        shortest = 0
        for i in range(1, len(strs)):
            if len(strs[i-1]) > len(strs[i]):
                shortest = i
        shortest_str = strs[shortest]
        
        # tail = len(strs[shortest-1])
        # for i in range(len(strs)):
        #     curr = strs[i]
        #     for j in range(len(shortest_str)-1, -1, -1):
        #         if j != shortest and curr[j] != shortest_str[j]:
        #             tail = j
                
            
        '''
        Binary search version 
        '''
        for i in range(len(strs)):
            left, right = 0, len(strs[shortest-1])
            
            while left <= right:
                mid = left + (right-left)//2
                
                if strs[i][mid] != shortest_str[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return 
                
        
        
        
        
#         i, ptr = 0, len(strs[0])-1
#         anext = 1
#         while anext < len(strs) and ptr >= 0:
#             alen = min(len(strs[anext]), len(strs[anext-1]))
#             i = 0
#             while  i < alen and i <= ptr:
#                 if strs[anext][i] != strs[anext-1][i]:
#                     break
#                 i += 1
#             ptr = i - 1
#             if ptr < 0:
#                 return ""
#             anext += 1
#         return strs[0][:ptr+1]
            
            
            
                
                