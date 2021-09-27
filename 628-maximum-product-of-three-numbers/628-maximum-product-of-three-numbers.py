class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Approach 3: choosing 2 smallest and 3 biggest ones
        # return the biggest product
        first_smallest, second_smallest = 1001, 1001
        first_biggest, second_biggest, third_biggest = -1001, -1001, -1001
        for i in range(len(nums)):
            if first_smallest > nums[i]:
                second_smallest = first_smallest
                first_smallest = nums[i]
            elif second_smallest > nums[i]:                    
                second_smallest = nums[i]
   
            if first_biggest < nums[i]:
                third_biggest = second_biggest
                second_biggest = first_biggest
                first_biggest = nums[i]
            elif second_biggest < nums[i]:
                third_biggest = second_biggest
                second_biggest = nums[i]
            elif third_biggest < nums[i]:
                third_biggest = nums[i]
         
        choice1 = first_smallest * second_smallest * first_biggest
        choice2 = first_biggest * second_biggest * third_biggest
        if choice1 > choice2:
            return choice1
        return choice2
        
        
        # Approach 2: Using sort 
        # Time and space complexities: O(nlogn), O(1)
        # This approach didn't work as still I didn't consider well about negative numbers
        # even if the array is sorted, in a list containing negative numbers the beginning part will include them and I need to consider which result would bring me to the bigger product
        # This approach is = sort + greedy
#         nums.sort()
#         first, second, third = nums[0], -1001, -1001
#         if nums[0] < 0:
#             i, j = 0, len(nums)-1
#             while i < 2 and j != i:
#                 if -nums[i] > first:
#                 i += 1
#                 j -= 1
    
        # Approach 1:
        # Tried to solve with determining 3 numbers and keep choosing bigger ones in a loop
        # This method does not work for negative numbers
        '''  
        first, second, third = -1001, -1001, -1001

            for num in nums:
                if abs(num) > first:
                    third = second
                    second = first
                    first = num
                elif abs(num) > second:
                    third = second
                    second = num
                elif abs(num)  > third:
                    third = num

            print(f'first {first} second {second} and third {third}')
            return first*second*third
        '''