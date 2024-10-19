from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        def find_max_distance_to_water(land_cells):
            max_dist = 0
            n = len(grid)
            q = deque([(i, j, 0) for i, j in land_cells])  # Include distance in the queue
            visited = set(land_cells)

            while q:
                i, j, dist = q.popleft()
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r, c = i + dx, j + dy
                    if 0 <= r < n and 0 <= c < n and (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c, dist + 1))
                        if grid[r][c] == 0:  # Found a water cell
                            max_dist = max(max_dist, dist + 1)

            return max_dist
        
        
        n = len(grid)
        land_cells = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]

        if not land_cells or len(land_cells) == n * n:  # All water or all land
            return -1

        return find_max_distance_to_water(land_cells)