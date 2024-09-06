class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def dfs(i,j):
            if min(i,j) < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return

            visited.add((i,j))
            directions = [(+1,0),(0,+1),(-1,0),(0,-1)]
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                if not (new_i, new_j) in visited:
                    dfs(new_i,new_j)


        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if not (r,c) in visited and grid[r][c] == '1':
                    print(r,c)
                    dfs(r,c)
                    islands += 1
        return islands
