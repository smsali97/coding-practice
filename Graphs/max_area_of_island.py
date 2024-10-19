class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # iterate over every unvisited island
            # for each island keep a running counter of how much nodes you
                # encounter, once you have visited all the nodes check if it
                # exceed maxmimum

        max_area = 0
        visited = set()
        directions = [ (1,0) , (-1,0) , (0,1) , (0,-1)  ]
        if not len(grid): return max_area
        m, n = len(grid), len(grid[0])
        
        def dfs(i,j):
            area = 1
            visited.add((i,j)) # visit node

            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                if new_i not in range(m): continue
                if new_j not in range(n): continue
                if (new_i,new_j) in visited: continue
                if grid[new_i][new_j] != 1: continue
                area += dfs(new_i,new_j) # 1 + rec. connections

            return area


        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j] == 1:
                    max_area = max(max_area,dfs(i,j))
        return max_area
