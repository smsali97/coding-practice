import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Finds the minimum effort required to traverse a grid from the top-left 
        to the bottom-right corner.

        Args:
          heights: A 2D list representing the grid of heights.

        Returns:
          The minimum effort required.
        """

        if len(heights) == 0: 
            return 0

        ROWS, COLS = len(heights), len(heights[0])
        START, END = (0, 0), (ROWS - 1, COLS - 1)

        # Use a min-heap to prioritize nodes with lower effort
        heap = [(0, START)]  # (effort, node)
        visited = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while heap:
            effort, node = heapq.heappop(heap)
            if node == END:
                return effort  # Reached the destination

            if node in visited:
                continue
            visited.add(node)

            for dx, dy in directions:
                r, c = node[0] + dx, node[1] + dy
                if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited:
                    new_effort = max(effort, abs(heights[r][c] - heights[node[0]][node[1]]))
                    heapq.heappush(heap, (new_effort, (r, c)))

        return 0  # Should not reach here if the grid is valid