class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Approach 1: H-index with while loop
        # i = 0
        # nums.sort(reverse=True)
        # while i < len(nums) and nums[i] > i:
        #     i += 1
        # if i < len(nums) and i == nums[i]:
        #     return -1
        # return i
        
        
        # Approach 2: Optimized first approach with Binary Search
        # nums.sort(reverse=True)
        # left, right = 0, len(nums)
        # while left < right:
        #     mid = left + (right - left)//2
        #     if mid < nums[mid]:
        #         left = mid + 1
        #     else:
        #         right = mid
        # if left < len(nums) and nums[left] == left:
        #     return -1
        # return left
        
        
        # Approach 3: Using count sort with slight addition
        # Time complexity: O(n)
        # Space complexity: O(n)
        alen = len(nums)
        count = [0]*(alen+1)
        for num in nums:
            if alen < num:
                count[alen] += 1
            else:
                count[num] += 1
        i = len(count)-1
        while i > 0:
            if count[i] == i:
                return i
            count[i-1]+=count[i]
            i -= 1
        return -1
        