class Solution:
    def reverse(self, arr, start, end):
        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1
    
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 2:
        # In-place approach with O(k*n) time complexity
        length = len(arr)
        k = k % length
        
        # reverse entirely
        i, j = 0, length-1
        Solution().reverse(arr, i, j)
        
        # reverse the left chunk => arr[:k]
        i = 0
        j = k - 1
        Solution().reverse(arr, i, j)

        # reverse the right chunk => arr[k:]
        i = k
        j = length - 1
        Solution().reverse(arr, i, j)
        
        
        
        # Approach 1:
        # Using extra space
        # Space complexity: O(n)
        # Time complexity: O(n)
        # length = len(arr)
        # k = k % length
        # ptr = length - k
        # i = 0
        # result = []
        # while ptr < length and i < length:
        #     result.append(arr[ptr])
        #     ptr = (ptr + 1) % length
        #     i += 1
        # length = len(result)
        # i = 0
        # while i < length:
        #     arr[i] = result[i]
        #     i += 1
        
        