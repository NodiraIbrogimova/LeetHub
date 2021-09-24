class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # Approach 1: After solving "Find Pivot Index" task
        # and reviewewing answes in discussion
        '''
        prefix_sum = [nums[0]]
        i = 1
        while i < len(nums):
            prefix_sum.append(prefix_sum[i-1]+nums[i])
            i += 1
        
        asum = prefix_sum[len(prefix_sum)-1]
        left, right = 0, (asum - nums[0])
        i = 0
        while left != right and i < len(nums)-1:
            i += 1
            left = prefix_sum[i-1]
            right = asum - left - nums[i]
        if left == right:
            return i
        return -1
        '''
        
        # Approach 2: with review
        postfixsum = sum(nums)
        pivot = 0
        prefixsum = 0
        while pivot < len(nums):
            postfixsum -= nums[pivot]
            
            if postfixsum == prefixsum:
                return pivot
            
            prefixsum += nums[pivot]
            pivot += 1
        return -1 