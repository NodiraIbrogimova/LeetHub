class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        # Approach 1
        # This technique uses two pointer i and j
        # Increments the sum of left part and right part until any or both of them equal avg_sum
        # Didn't use this approach as needed 3 if cases block in while loop - takes time
        # Rather looping over the whole array seems to be less time consuming
        
        '''
        asum = sum(arr) // 3
        i, j = 0, len(arr)
        left, right = 0, 0
        while i + 1 < j and arr[i] != arr[j]:
            arr[i] += left
            arr[j] += right
            
            i += 1
            j -= 1
        '''
        
        # Approach 2
        # Loop throught the array, calculate avg_sum
        # if avg_sum isn't divisible by 3, means we cannot partition it into three equal parts
        # else loop and increment counter once the partition sum gets equal to avg_sum
        avg_sum = sum(arr) / 3
        if avg_sum % 1 != 0:
            return False
        curr_total = 0
        counter = 0
        i = 0
        
        while i < len(arr):
            curr_total += arr[i]
            if curr_total == avg_sum:
                curr_total = 0
                counter += 1
            i += 1
        return counter >= 3
        