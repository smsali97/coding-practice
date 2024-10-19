class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        max_gold = 0
        
        def explore(i,j,visited=set(),gold_so_far=0):
            # colect gold greedily
            gold_so_far += grid[i][j]
            
            # we can stop anywhere
            nonlocal max_gold
            max_gold = max(max_gold,gold_so_far)
            
            visited.add((i,j))
            for dx, dy in directions:
                r = dx + i
                c = dy + j
                # explore frontier that is not visited and with a non-zero gold
                if r not in range(m) or c not in range(n): continue
                if (r,c) in visited or grid[r][c] == 0: continue
                explore(r,c,visited,gold_so_far)
            visited.remove((i,j))

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                     # start ->  multiple source DFS stop anywhere -> keep track of running max > max_gold
                    explore(i,j)
        return max_gold