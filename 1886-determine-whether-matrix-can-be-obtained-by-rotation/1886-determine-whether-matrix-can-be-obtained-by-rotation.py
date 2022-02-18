class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if len(mat) != len(target):
            return False
        
        n = len(mat)
        temp = None
        times = 4
        while times >= 0:
            times  -= 1
            has_unmatch = False
            for i in range(n//2):
                for j in range(i, (n-i-1)):
                    temp = mat[i][j]
                    mat[i][j] = mat[j][n-i-1]
                    mat[j][n-1-i] = mat[n-i-1][n-j-1]
                    mat[n-i-1][n-j-1] = mat[n-j-1][i]
                    mat[n-j-1][i] = temp
            row, col = 0, 0
            while row<n:
                col = 0
                while col<n:
                    if mat[row][col] != target[row][col]:
                        has_unmatch = True
                        col, row = n, n
                        break
                    col += 1
                row += 1
            if not has_unmatch:
                return True
        return False
    
        '''
        [[0,0],[1,0]]
        [[1,0],[0,0]]
        
        [[0,1],[1,0]]
        [[1,0],[0,1]]
        
        [[0,1],[1,1]]
        [[1,0],[0,1]]
        
        [[0,0,0],[0,1,0],[1,1,1]]
        [[1,1,1],[0,1,0],[0,0,0]]
        
        [[0,0],[0,1]]
        [[0,0],[1,0]]
        Columns should become rows
        For 
        [0] [1]          [1, 0]
        [1] [0]    ----> [0, 1]
        At most we can rotate 3 times, at fourth time the grid takes original position
        After rotating the originat mat each time, compare the result with target
        '''