class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Warm-up: Approach 2
        '''
        [1,]
        '''
        left, right = 0, 1
        while right < len(nums):
            if nums[left] < nums[right]:
                nums[left+1] = nums[right]
                left += 1
            right += 1
        return left+1
        
        
        if len(nums) <= 1:
            return len(nums)
        left, right = len(nums)-1, len(nums)-2
        while left >= 0:
            if nums[left] == nums[right]:
                nums[right] = '_'
            right = left
            left -= 1
        left, right = 0, 0
        while right < len(nums):
            if nums[right] == '_':
                while nums[right] == '_':
                    right += 1
                    if right == len(nums):
                        break
                else:
                    nums[left+1], nums[right] = nums[right], nums[left+1]
                    left += 1
                    continue
            right += 1
        right = len(nums)-1
        while right >= 0 and nums[right] == '_':
            right -= 1
        return right+1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # Approach 1
        # left, right = 0, 1
        # while right < len(nums):
        #     if nums[left] < nums[right]:
        #         left += 1
        #         nums[left] = nums[right]
        #     right += 1
        # return left + 1