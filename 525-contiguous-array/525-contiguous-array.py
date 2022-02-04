class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length =0
        hash={}
        count=0
        for i in range(len(nums)):
            current=nums[i]
            if current==0:
                count-=1 # decrement our count if our current element is 0
            else:
                # increment our count if current element is 1
             count+=1

            if count==0:
                # if count is 0, we have a new subarray with length+1
                max_length=i+1
            if count in hash:
                max_length=max(max_length,i-hash[count]) 
            else:
                hash[count]=i
        return max_length
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i-1]
        # print('prefix sum is: ', nums)
        # for i in range(len(nums)-1, -1, -1):
        #     if (i+1) - nums[i]*2 >= 0:
        #         return nums[i] * 2
        # return 0
            
            