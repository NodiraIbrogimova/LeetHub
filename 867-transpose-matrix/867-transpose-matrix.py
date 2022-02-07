class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        t_rows, t_cols = cols, rows
        transposed = [[None]*rows for _ in range(cols)]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                transposed[col][row] = matrix[row][col]
        return transposed