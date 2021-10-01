from collections import deque
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        '''
        1. numRows => grid.length == numRows
           curr_row = grid[row]
           
             1
            1 1
           1 2 1        
          1 3  3 1
         1 4 6 4 1
        1 5 10 10 5 1
       1 6 15 20 15 6 1
      1 7 21 35 35 21 7 1
           
        
        1. Brute-force
        2. Optimize
        '''
        grid = [[1]]
        
        if numRows == 1:
            return grid
        row = 1
        while row < numRows:
            left = 0
            right = left + 1
            result = deque([])
            while right < len(grid[row-1]):
                result.append(grid[row-1][left] + grid[row-1][right])
                left += 1
                right += 1
            result.append(1)
            result.appendleft(1)
            grid.append(result)
            row += 1
        return grid
        
        
        
        
        
    
    
        
        