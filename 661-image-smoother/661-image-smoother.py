class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
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
                if row+1 < len(smoothed_M):
                    if col+1 < len(smoothed_M[row]):
                        # add value at the bottom diagonal
                        asum += M[row+1][col+1]
                        neighbors += 1
                    if col - 1 >= 0:
                        asum += M[row+1][col-1]
                        neighbors += 1
                    # add value at the bottom
                    asum += M[row+1][col]
                    neighbors += 1
                if col-1 >= 0:
                    asum += M[row][col-1]
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
        