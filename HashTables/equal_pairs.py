class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def key(arr):
            return '-'.join(list(map(str,arr)))
        from collections import defaultdict
        checker = defaultdict(int)
        for row in grid:
            checker[ key(row) ] += 1
        pairs = 0
        for c in range(len(grid[0])):
            col_val = key([grid[i][c] for i in range(len(grid)) ])
            pairs += checker[col_val]
        return pairs
