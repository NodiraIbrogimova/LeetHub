class Solution:
    def getCurrentRange(self, end, start):
        if end - start > 0:
            temp = str(start) + '->' + str(end)
        else:
            temp = str(start)
        return temp
    
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Warm-up
        if not nums:
            return nums
        
        start, i = nums[0], 1
        curr, result = start, list()
        while i < len(nums):
            curr += 1
            if curr != nums[i]:
                temp = self.getCurrentRange(nums[i-1], start)
                result.append(temp)
                start = nums[i]
                curr = start
            i += 1
        temp = self.getCurrentRange(nums[i-1], start)
        result.append(temp)
        return result
        
        # Approach 1
        if not len(nums):
            return nums
        result = []
        smallest = 0
        i = smallest + 1
        prev = nums[smallest]
        while i < len(nums):
            prev = nums[i-1]
            if nums[i] - prev > 1:
                if smallest < i-1:
                    result.append(f'{nums[smallest]}->{nums[i-1]}')
                else:
                    result.append(f'{nums[smallest]}')
                smallest = i
            i += 1
        i -= 1
        if nums[smallest] != nums[i]:
            result.append(f'{nums[smallest]}->{nums[i]}')
        else:
            result.append(f'{nums[smallest]}')
        return result
        
        