class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # warm-up
        # use a count sort learned from monday weekly shared by mentor Mudin
        amax = max(heights)
        count = [0]*(amax+1)
        for index, value in enumerate(heights):
            count[value] += 1
        i, j = 0, 0
        total = 0
        while i < len(count):
            if count[i] > 0:
                if heights[j] != i:
                    total += 1
                count[i] -= 1
                j += 1
            else:
                i += 1
        return total
        
        # Approach 2
        # Use another implementation of Count Sort
        # Time: O(n+k)
        # Space: O(n+k)
        expected = [0]* len(heights)
        
        count = [0]*(max(heights)+1)
        
        for i in range(len(heights)):
            count[heights[i]] += 1
        
        for i in range(1, len(count)):
            count[i] += count[i-1]
        
        unmatch = 0
        for height in heights:
            count[height] -= 1
            expected[count[height]] = height
            if expected[count[height]] != heights[count[height]]:
                unmatch += 1
        
        del expected
        return unmatch
    
        # Approach 1
        # The case of Count Sort Algorithm shown in Harward lectures doesn't work in this case:
        max_val = max(heights)
        freq = [0]*(max_val+1)
        for height in heights:
            freq[height] += 1
        total = max_val + 1
        i = len(freq)-1
        while i >= 0:
            freq[i] = total - freq[i]
            total = freq[i]
            i -= 1
        expected = [0]*len(heights)
        for height in heights:
            expected[freq[height]] = height
            freq[height] += 1
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count
        