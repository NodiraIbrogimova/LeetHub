class Solution:
    def is_inrange(self, position, border):
        return not (position < 0 or position >= border)
    
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # Approach 2
        # Using hashtable to calculate the existance of neighbor
        # at row (r,c): 
        # (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r,c), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)
        filtered = [[0]*len(img[0]) for _ in range(len(img))]
        rows = [-1,-1,-1,0,0,0,1,1,1]
        cols = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        for row in range(len(img)):
            for col in range(len(img[0])):
                total, neighbors_count = 0, 0
                for i in range(9):
                    curr_row = row + rows[i]
                    curr_col = col + cols[i]
                    
                    if self.is_inrange(curr_row, len(img)) and self.is_inrange(curr_col, len(img[0])):
                        total += img[curr_row][curr_col]
                        neighbors_count += 1
                filtered[row][col] = total//neighbors_count
        return filtered
        '''
        rows = [-1,-1,-1,0,0,0,1,1,1]
        cols = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        
        for i in range(-1,2): # -1 0 1
            for j in range(-1,2): # -1 0 1
                nr = r + i
                nc = c + j
                if (nr < 0 || nr >= m) continue
                if (nc < 0 || nc >= n) continue
                
        OR
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                nr = row + rows[i]
                nr = col + cols[j]
                
                if (nr < 0 || nr >= m) continue
                if (nc < 0 || nc >= n) continue
        
        '''
        # Approach 1
        # Checking nine sides manually each time with if cases
        smoothed_M = deepcopy(M)
        row = 0
        while row < len(smoothed_M):
            col = 0
            while col < len(smoothed_M[0]):
                asum = 0
                neighbors = 1
                # check current for neighbors
                if col+1 < len(smoothed_M[row]):
                    asum += M[row][col+1]
                    neighbors += 1
                if col-1 >= 0:
                    asum += M[row][col-1]
                    neighbors += 1
                    
                if row+1 < len(smoothed_M):
                    if col+1 < len(smoothed_M[row]):
                        # add value at the bottom diagonal
                        asum += M[row+1][col+1]
                        neighbors += 1
                    if col-1 >= 0:
                        asum += M[row+1][col-1]
                        neighbors += 1
                    # add value at the bottom
                    asum += M[row+1][col]
                    neighbors += 1
                
                if row-1 >= 0:
                    if col-1 >= 0:
                        # add value at the top diagonal
                        asum += M[row-1][col-1]
                        neighbors += 1
                    if col+1 < len(M[0]):
                        # add value at the top diagonal
                        asum += M[row-1][col+1]
                        neighbors += 1
                    # add value at the top
                    asum += M[row-1][col]
                    neighbors += 1
                asum += M[row][col]
                smoothed_M[row][col] = math.floor(asum/neighbors)
                col += 1
            row += 1
        return smoothed_M
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # x_len = len(M)
        # y_len = len(M[0]) if x_len else 0
        # res = deepcopy(M)
        # for x in range(x_len):
        #     for y in range(y_len):
        #         neighbors = [
        #             M[_x][_y]
        #             for _x in (x-1, x, x+1)
        #             for _y in (y-1, y, y+1)
        #             if 0 <= _x < x_len and 0 <= _y < y_len
        #         ]
        #         res[x][y] = sum(neighbors) // len(neighbors)
        # return res
        