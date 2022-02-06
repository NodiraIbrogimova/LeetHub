class Solution:
    perimeter = 0
    def sumPerimeter(self, row, col, grid):
        if col - 1 < 0:
            self.perimeter += 1
        elif grid[row][col-1] == 0:
            self.perimeter += 1
            
        if col + 1 >= len(grid[row]):
            self.perimeter += 1
        elif grid[row][col+1] == 0:
            self.perimeter += 1
        
        if row - 1 < 0:
            self.perimeter += 1
        elif grid[row-1][col] == 0:
            self.perimeter += 1
            
        if row + 1 >= len(grid):
            self.perimeter += 1
        elif grid[row+1][col] == 0:
            self.perimeter += 1
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = 0,0
        while row < len(grid):
            
            while col < len(grid[row]):
                land = grid[row][col]
                if not land:
                    col += 1
                    continue
                # check four sides
                self.sumPerimeter(row, col, grid)
                col += 1
            col = 0
            row += 1
        
        return self.perimeter
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        grid_ext = ['0' + ''.join(str(x) for x in row) + '0' for row in grid]
        grid_trans = list(map(list, zip(*grid)))
        grid_ext += [ '0' + ''.join(str(x) for x in row) + '0' for row in grid_trans ]                
        return sum(row.count('01') + row.count('10') for row in grid_ext)
        
        