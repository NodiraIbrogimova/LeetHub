class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        # Approach 1
        # Use start as the point for the subarray
        # Change start pointer to right only when the array starts to fall in value
        # Time: O(n)
        # Space: O(1)
        left, right = 0, 1
        start = left
        maxlength = 1
        while right < len(nums):
            if nums[right] <= nums[left]:
                maxlength = max(maxlength, right-start)
                start = right
            left = right
            right += 1
        return max(maxlength, right-start)