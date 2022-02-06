class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        # warm-up
        # check is rxc is possible
        if (r*c != len(nums)*len(nums[0])) or (r == len(nums) and c == len(nums[0])):
            return nums
        reshaped = []
        for row in range(r):
            reshaped.append([0]*c)
        nums_row, nums_col = 0, 0
        row, col = 0, 0
        while row < r:
            while col < c:
                reshaped[row][col] = nums[nums_row][nums_col]
                col += 1
                nums_col += 1
                if nums_col == len(nums[0]):
                    nums_col = 0
                    nums_row += 1
            col = 0
            row += 1
        return reshaped
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # flat = sum(nums, [])
        # if len(flat) != r * c:
        #     return nums
        # tuples = zip(*([iter(flat)] * c))
        # return map(list, tuples)
        