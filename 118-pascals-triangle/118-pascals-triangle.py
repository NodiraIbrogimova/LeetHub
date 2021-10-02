from collections import deque
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Approach 2: Optimization with answer in discuss part
        pascal_tri = []
        row, col = 0, 0
        while row < numRows:
            result = []
            col = 0
            while col < row + 1:
                if col == 0 or col == row:
                    result.append(1)
                else:
                    left = pascal_tri[row-1][col-1]
                    right = pascal_tri[row-1][col]
                    result.append(left+right)
                col += 1
            pascal_tri.append(result)
            row += 1
        return pascal_tri

        # Approach 1: Brute-force solution
        '''
             1
            1 1
           1 2 1        
          1 3 3 1
         1 4 6 4 1
        1 5 10 10 5 1
       1 6 15 20 15 6 1
      1 7 21 35 35 21 7 1
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
            grid.append(deque([1]) + result + deque([1]))
            row += 1
        return grid
    # Time complexity: O(n*m)
    # Space complexity: O(30) - O(1)