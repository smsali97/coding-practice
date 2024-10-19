class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        from collections import deque

        def bfs(i,j):
            q = deque([(i,j,0,set())])
            while q:
                i,j,dist,visited = q.popleft()
                print(i,j)
                visited.add((i,j))
                dist += 1

                directions = [(+1,0),(-1,0),(0,+1),(0,-1)]
                for dx, dy in directions:
                    new_i = dx + i
                    new_j = dy + j
                    if (new_i,new_j) in visited: continue
                    if new_i not in range(len(grid)): continue
                    if new_j not in range(len(grid[new_i])): continue
                    if grid[new_i][new_j] == -1: continue
                    if grid[new_i][new_j] == 0:
                        return dist
                    q.append( (new_i,new_j,dist,visited) )
            return INF
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                    if grid[i][j] == INF: # land
                        grid[i][j] = bfs(i,j)

        
            