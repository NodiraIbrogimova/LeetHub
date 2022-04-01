class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        '''
        [3,1,2,2,2,1,3]
        
        
        '''
        # Approach 1
        # Brute-force
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i*j % k == 0:
                    count += 1
        return count