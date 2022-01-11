class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Warm-up
        
        '''
        [1,  0,  0,  1,  1,  1,  0]
        --           s              c
        
        '''
        start, curr = 0, 0
        amax = 0
        while curr < len(nums):
            if nums[curr] == 0:
                amax = max(amax, curr-start)
                start = curr+1
            curr += 1
        return max(amax, curr-start)
        
        # Approach 1
        amax, count = 0, 0
        for num in nums:
            is_one = num & 0b00000001
            if not is_one:
                if count > amax:
                    amax = count
                count = 0
            else:
                count += 1
        if count > amax:
            return count
        return amax
        