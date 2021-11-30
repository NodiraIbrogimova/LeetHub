class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = dict()
        for i in range(len(nums)):
            if nums[i] in hashmap and abs(hashmap[nums[i]] - i) <= k:
                return True
            hashmap[nums[i]] = i
        return False
        