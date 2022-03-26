class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''
        The repetition can be in the beginning, middle or end
        One detail given is: the number must start from 1
        
        if in the beginning, 1 is not there
        
        take for example three numbers:
        a b c 
        the comparison should be like: 
        a < b < c
        if a == b and b < c:
            then repeated number is b and missing number is b-1
        elif a < b and b == c:
            then repeated number is b and missing number is b + 1
        
        As we can see, in any case the repeated number is b, but the number missing depends on the nighbors
        
         f s -1
        [2,2]
        if first and second are equal, means the repetition in at the beginning. So return [second, second-1]
        
        
        [2,3,2]      
        '''
        seen_value = None
        amax = 10000
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                seen_value = nums[i]
            else:
                seen.add(nums[i])
        for i in range(1, amax+1):
            if i not in seen:
                return [seen_value, i]