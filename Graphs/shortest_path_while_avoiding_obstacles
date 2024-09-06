from collections import deque
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def invalid_point(r, c, grid):
            return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        visit = set()
        q.append(((0, 0), 0, k))

        while q:
            (r, c), cost, lifelines = q.popleft()
            if (r, c) == (len(grid) - 1, len(grid[0]) - 1):
                return cost

            if (r, c, lifelines) in visit:
                continue

            visit.add((r, c, lifelines))

            for dr, dc in directions:
                r_i, c_i = r + dr, c + dc
                if invalid_point(r_i, c_i, grid):
                    continue

                new_lifelines = lifelines - grid[r_i][c_i]
                if new_lifelines >= 0 and (r_i, c_i, new_lifelines) not in visit:
                    q.append(((r_i, c_i), cost + 1, new_lifelines))

        return -1
