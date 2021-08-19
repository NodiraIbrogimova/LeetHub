class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Approach 1
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        # create result list
        # iterate through the indices list and insert chars:
        # result[indices[i]] = s[i]
        # return string version of the result: ““.join(result)

        '''
        shuffled_list = [None]*len(s)
        i = 0
        while i < len(s):
            shuffled_list[indices[i]] = s[i]
            i += 1
        return "".join(shuffled_list)
        '''
        
        
        # Approach 2
        s = list(s)
        # The idea is:
        # If the indices list is sorted, the s gets sorted as well.
        cur = 0
        while cur < len(indices):
            # print('indices[i]: ', indices[i], i)
            if cur == indices[cur]:
                cur += 1
                continue
            newIndex = indices[cur]
            s[cur], s[newIndex] = s[newIndex], s[cur]
            indices[cur], indices[newIndex] = indices[newIndex], indices[cur]
        return "".join(s)

