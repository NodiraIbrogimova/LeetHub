class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Approach 1:
        # Find values smaller than target
        # Check the length of the values smaller with the length of the array
        # the target array is a lit of values starting from [len(arr)-count:target_count
        target_count, smallar_vals_count = 0, 0
        for num in nums:
            if num < target:
                smallar_vals_count += 1
            elif num == target:
                target_count += 1
        
        result = []
        for i in range(smallar_vals_count, target_count + smallar_vals_count):
            result.append(i)
        return result
        
        
        