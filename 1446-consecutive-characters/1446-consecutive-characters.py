class Solution:
    def maxPower(self, s: str) -> int:
        
        # Approach 2
        # Count the consecutive char and once different chars are met, update maxCount if bigger than the curr_count
        curr_count, max_count = 0, 0
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                curr_count += 1
            else:
                max_count = max(curr_count, max_count)
                curr_count = 0
        return max(max_count+1, curr_count+1)
                
                
        
        # Approach 1
        # As the domain of the chars are only lowercase English letters, we use a counter array with a length of 26 to count the frequency of the repeated substring chars
        # Return the max of the counter array as the power
        # Time: O(n)
        # Space: O(26) -> O(1) for an array of 26
        if len(s) == 1:
            return 1
        count = [0]*26
        a = ord('a')
        prev, curr = 0, 1
        while curr < len(s):
            if s[curr] != s[prev]:
                prev_char = ord(s[prev])
                count[prev_char - a] = max(curr - prev, count[prev_char - a])
                prev = curr
            curr += 1
        if prev < len(s) - 1:
            prev_char = ord(s[prev])
            count[prev_char - a] = max(curr - prev, count[prev_char - a])
        return max(count)
        