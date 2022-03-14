class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, el in enumerate(nums):
            if i % 10 == el:
                return i
        return -1