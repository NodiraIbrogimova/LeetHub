class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i = 1
        operations = 0
        while i < len(nums):
            if nums[i] <= nums[i-1]:
                diff = (nums[i-1] - nums[i] + 1)
                nums[i] += diff
                operations += diff
            i += 1
        return operations
        