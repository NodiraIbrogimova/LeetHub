class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        print('\nfor: ', indices)
        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]
        count = 0
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        for i in range(m):
            for j in range(n):
                if (rows[i]+cols[j]) % 2 != 0:
                    count += 1
        return count