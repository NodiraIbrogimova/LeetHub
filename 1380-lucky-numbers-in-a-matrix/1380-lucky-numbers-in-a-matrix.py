class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        '''
        1. Find min for each row
        2. And max for each col
        3. Compare if mins == maxs
        Let amax be the maximum of row minimums and amin be the minimum of column maximums. If they are equal then this single number is the only lucky number, otherwise no lucky number exists.
        Questions:
        1. Are there any equal numbers present in an input grid?
        '''
        amin = float('-inf')
        amax = float('inf')
        for row in range(len(matrix)):
            max_min = 2**32-1
            for col in range(len(matrix[0])):
                max_min = min(max_min, matrix[row][col])
            amin = max(amin, max_min)
        for col in range(len(matrix[0])):
            max_int = -2**32-1
            for row in range(len(matrix)):
                max_int = max(max_int, matrix[row][col])
            amax = min(amax, max_int)
        if amin == amax:
            return [amin]
        return []
                
                
        