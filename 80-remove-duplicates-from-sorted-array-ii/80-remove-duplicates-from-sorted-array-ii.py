class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ''' 
        [1,1,1,2,2,3]
        '''
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
        seen = False
        left, right = 0, 1
        # last = len(nums)-1
        # prev = nums[left]
        while right < len(nums):
            if right < len(nums) and nums[left] == nums[right]:
                if seen:
                    while right < len(nums) and nums[right] != nums[left]:
                        right += 1
                    if right < len(nums):
                        left += 1
                        nums[left] = nums[right]
                        nums[right] = None
                    seen = False
                else:
                    seen = True
            left = right
            right += 1
        left, right = 0, 0
        while right < len(nums):
            if nums[left] == None:
                while right < len(nums) and nums[right] != None:
                    right += 1
                if right < len(nums):
                    nums[left], nums[right] = nums[left], nums[right]
            elif nums[right] == None:
                temp = right
                while right < len(nums) and nums[right] != None:
                    right += 1
                nums[temp], nums[right] = nums[right], nums[temp]
            left = right
            right += 1
        return nums
                
        
        