class Solution:
    def countSort(self, A, k):
        
        # create an integer list of size `n` to store the sorted list
        output = [0] * len(A)
    
        # create an integer list of size `k + 1`, initialized by all zero
        freq = [0] * (k + 1)
    
        # using the value of each item in the input list as an index,
        # store each integer's count in `freq[]`
        for el in A:
            freq[el] = freq[el] + 1
    
        # calculate the starting index for each integer
        total = 0
        for i in range(k + 1):
            oldCount = freq[i]
            freq[i] = total
            total += oldCount
    
        # copy to the output list, preserving the order of inputs with equal keys
        for el in A:
            output[freq[el]] = el
            freq[el] = freq[el] + 1
    
        # copy the output list back to the input list
        i = len(A) - 1
        j = 0
        while i >= 0:
            A[j] = output[i]
            j += 1
            i -= 1
        print('sorted: ', A)
        return A

    def minSubsequence(self, nums):
        k = 0
        asum = 0
        result = 0
        for el in nums:
            asum += el
            if k < el:
                k = el
        nums = Solution().countSort(nums, k)
        for i in range(len(nums)):
            num = nums[i]
            result += num
            if result > asum - result:
                return nums[:i+1]