class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row, col = 0, 0
        while row < len(matrix):
            curr_row = row + 1
            while col < len(matrix[0]):
                curr_col = col+1
                while curr_row < len(matrix) and curr_col < len(matrix[row]):
                    if matrix[curr_row-1][curr_col-1] != matrix[curr_row][curr_col]:
                        return False
                    curr_row += 1
                    curr_col += 1
                curr_row = row + 1
                col += 1
            col = 0
            row += 1
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
        #            for r, row in enumerate(matrix)
        #            for c, val in enumerate(row))
        