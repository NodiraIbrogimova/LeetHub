class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        '''
        (i * j) is divisible by k, if either i or j is divisible by k
        - As looking for pairs, check for numbers with freq > 1
        - count array holding freq of each num in nums
        - if count is > 1, doesn't matter where this values are, 
        every time there will be i < j possibility. But, we should find if i or j is divisible by k
        '''
        MAX_LENGTH = 100
        freq = [[] for i in range(MAX_LENGTH+1)]
        for index, num in enumerate(nums):
            freq[num].append(index)
        count, excluded = 0, 0
        for indexes in freq:
            excluded = 0
            for i in range(len(indexes)):
                for j in range(i+1, len(indexes)):
                    if indexes[i]*indexes[j] % k == 0:
                        count += 1
        return count
    
        # Approach 1
        # Optimized Brute-force 
#         hashmap = dict()
#         count = 0
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j] and (i % k == 0 or j % k == 0):
#                     count += 1
#         return count
    
    
#         # Approach 1
#         # Brute-force
#         count = 0
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j] and (i % k == 0 or j % k == 0):
#                     count += 1
#         return count