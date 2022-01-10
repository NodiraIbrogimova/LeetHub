class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Warm-up
        MIN_NUM = -2**32-1
        first, second, third = MIN_NUM, MIN_NUM, MIN_NUM
        for num in nums:
            if num == first or num == second or num == third:
                continue
            
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        if third == MIN_NUM:
            return first
        return third
        
        
        
        
        
        
        
        
        
        # Approach 1
        amax, second_max, third_max = None, None, None
        
        for num in nums:
            if num == amax or second_max == num or third_max == num:
                continue
            if not amax or num > amax:
                third_max = second_max
                second_max = amax
                amax = num
            elif not second_max or num > second_max:
                third_max = second_max
                second_max = num
            elif not third_max or num > third_max:
                third_max = num
        if third_max == None:
            return amax
        return third_max