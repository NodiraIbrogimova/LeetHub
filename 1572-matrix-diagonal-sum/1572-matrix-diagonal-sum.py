class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        row, col = 0, 0
        total = 0
        while row < n:
            total += (mat[row][col] + mat[row][~col])
            row += 1
            col += 1
        if n & 1:
            total -= mat[n//2][n//2]
        return total