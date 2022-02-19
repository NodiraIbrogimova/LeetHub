class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    # left
                    if col > 0 and grid[row][col-1] == 1:
                        perimeter -= 2
                    # bottom
                    if row > 0 and grid[row-1][col] == 1:
                        perimeter -= 2				
                    perimeter += 4
        return perimeter