class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]

        grid[m-1][n-1] = 1 # base case
        # bottom to top
        for i in reversed(range(m)):
            # l to r
            for j in reversed(range(n)):
                bottom_val = grid[i+1][j] if i < m - 1 else 0 # bounds check
                right_val = grid[i][j+1] if j < n - 1 else 0 # bounds check
                grid[i][j] += bottom_val+right_val
        return grid[0][0]
