class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Warm-up
        hashmap = Counter(nums)
        max_length = 0
        for curr in hashmap:
            if hashmap.get(curr+1):
                max_length = max(max_length, hashmap[curr+1]+hashmap[curr])
            elif hashmap.get(curr-1):
                max_length = max(max_length, hashmap[curr-1]+hashmap[curr]) 
        return max_length

    
        # Approach 1
        hashmap = dict()
        longest_subs = 0
        i = 0
        while i < len(nums):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
            if hashmap.get(nums[i]+1):
                longest_subs = max(hashmap[nums[i]] + hashmap[nums[i] + 1], longest_subs)
            if hashmap.get(nums[i]-1):
                longest_subs = max(hashmap[nums[i]] + hashmap[nums[i] - 1], longest_subs)
            i += 1
        return longest_subs