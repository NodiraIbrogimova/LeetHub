class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first_min = 2**32-1
        second_min = 2**32-1
        first_max = -2**32-1
        second_max = -2**32-1

        i = 0
        while i < len(nums):

            if nums[i] < first_min or nums[i] < second_min:
                second_min = min(first_min, second_min)
                first_min = nums[i]

            if nums[i] > first_max or nums[i] > second_max:
                second_max = max(first_max, second_max)
                first_max = nums[i]

            i += 1
        return (first_max*second_max) - (first_min*second_min)

#         expected = [0]*len(nums)
#         count = [0]*(max(nums)+1)
        
#         for i in range(len(nums)):
#             count[nums[i]]+=1
        
#         for i in range(1, len(count)):
#             count[i] += count[i-1]
        
#         for num in nums:
#             count[num] -= 1
#             expected[count[num]] = num
        
#         length =  len(expected)
#         return (expected[length-1]*expected[length-2]) - (expected[0]*expected[1])

