class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Warm-up
        count, start, end = dict(), dict(), dict()
        for index, value in enumerate(nums):
            if value not in start: start[value] = index
            end[value] = index
            count[value] = count.get(value, 0) + 1
        
        max_count = max(count.values())
        min_length = len(nums)
        for val in count:
            if count[val] == max_count:
                min_length = min(min_length, end[val]-start[val]+1)
        return min_length
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Approach 2
        # Looking at Solution:
        # left stores the start points of the nums
        # right stores the end points of the nums
        # count stores the count of the nums
        start, count, end = dict(), dict(), dict()
        for index, num in enumerate(nums):
            if num not in start: start[num] = index
            end[num] = index
            count[num] = count.get(num, 0) + 1

        # search for a num with highest count and smallest end - start difference
        max_count = max(count.values())
        min_length = len(nums)
        for acount in count:
            if count[acount] == max_count:
                min_length = min(min_length, end[acount] - start[acount] + 1)
        return min_length
                
            
            
        
        
        
        
        # Approach 1
        # Doesn't work as this provides most biggest length not min length
        # Iterate through array, count the number of occurences for each number
        # for the number with most occurences, find start and end indeices
        '''
        hashmap = dict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        most_occured = 0
        count = 0
        # find biggest occurence
        for num in hashmap:
            if count < hashmap[num]:
                count = hashmap[num]
                most_occured = num
                
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] == most_occured:
                break
            start += 1
        while end > start:
            if nums[end] == most_occured:
                break
            end -= 1
        return end - start + 1
        '''
        