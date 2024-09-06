class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # start from all rotten oranges
        # spread that disease (4 directions) each step is +1
        # use bfs because minimum and all oranges have been exhausted
        def bfs(oranges,lst):
            from collections import deque
            q = deque(lst)
            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            time = 0
            while q and oranges:
                oranges_to_cater = len(q)
                for i in range(oranges_to_cater):
                    r,c = q.popleft()
                    for dx, dy in directions:
                        row = r + dx
                        col = c + dy
                        if row not in range(len(grid)): continue
                        if col not in range(len(grid[row])): continue
                        if grid[row][col] != 1: continue
                        q.append((row,col))
                        grid[row][col] = 2
                        oranges -= 1
                time += 1
            return -1 if oranges else time
                    
        # when is it impossible? if you cannot reach an orange cell and there are oranges left
        oranges = 0
        rotten_oranges = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    oranges += 1
                elif grid[i][j] == 2:
                    rotten_oranges.append((i,j))
        dist = bfs(oranges,rotten_oranges)
        return dist