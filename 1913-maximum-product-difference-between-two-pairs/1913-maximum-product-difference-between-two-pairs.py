class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        expected = [0]*len(nums)
        count = [0]*(max(nums)+1)
        
        for i in range(len(nums)):
            count[nums[i]]+=1
        
        
        for i in range(1, len(count)):
            count[i] += count[i-1]
            
        
        for num in nums:
            count[num] -= 1
            expected[count[num]] = num
            
        # print('expected is: ', expected)
        length =  len(expected)
        # print('expected is: ', expected)
        return expected[length-1]*expected[length-2] - expected[0]*expected[1]