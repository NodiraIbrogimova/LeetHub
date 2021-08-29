class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Approach 1: H-index with while loop
        i = 0
        nums.sort(reverse=True)
        while i < len(nums) and nums[i] > i:
            i += 1
        if i < len(nums) and i == nums[i]:
            return -1
        return i
        
        
        # Approach 2: Optimized first approach with Binary Search
        
        