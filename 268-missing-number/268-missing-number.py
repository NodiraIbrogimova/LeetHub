class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        amax = len(nums)
        curr = amax
        for i in range(len(nums)-1, -1, -1):
            if curr != nums[i]:
                return curr
            curr -= 1
        return curr