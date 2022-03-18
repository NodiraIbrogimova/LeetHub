class Solution:
    
    
    def sideIsPositive(self, p1_x, p1_y, p2_x, p2_y):
        return min(p1_y, p2_y) > max(p1_x, p2_x)
    
    
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return self.sideIsPositive(rec1[0], rec1[2], rec2[0], rec2[2]) and self.sideIsPositive(rec1[1], rec1[3], rec2[1], rec2[3])
    
        '''
                    |         .....b2
                    |
                    |         b1....x =(b2_y, b2_x-b1_x)
                    |    a2
                    |        
        ------------a1-------------
                    |
                    |
             a---|  |
                 |  |
                 a' |
                    |
                    

        
                    |
                    |
             a---|  |
                 |  |
                 a' |
                    |
                    |
        ------------0'-------------
                    |
                    |       .....x
                    |
                    |       x....x'
                    |    0
                    |        
        ------------0'-------------
                    
        1. If (x' - 0') is in (x' - x), that's:
        (x' - 0') < (x' - x)
        2. And one point's (p1) doesn't lie in the second point (p2)
        if (x1,x2) or (y1,y2) in (x1', x2') or (y1',y2')
        
        One rectangular lies inside another one
        '''
        # x'
        
            