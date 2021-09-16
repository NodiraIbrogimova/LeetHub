class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if hashmap[num] >= 2:
                return True
        return False
        