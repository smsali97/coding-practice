class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        global_max = 1  # Initialize to 1 (at least one cell itself)

        def dfs(i, j):
            if (i, j) in cache: 
                return cache[(i, j)]

            max_dist = 1  # Initialize max_dist for this cell
            for dx, dy in [(+1, 0), (-1, 0), (0, -1), (0, +1)]:
                r, c = i + dx, j + dy
                if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] > matrix[i][j]:
                    max_dist = max(max_dist, dfs(r, c) + 1)
            
            
            cache[(i, j)] = max_dist
            nonlocal global_max
            global_max = max(global_max, max_dist)
            
            return max_dist

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                dfs(i, j)  # No need to pass an initial distance

        return global_max