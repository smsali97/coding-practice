class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # elevation <= t [time]
        n = len(grid)
        start = (0,0)
        end = (n-1,n-1)

        # 0 2
        # 1 3
        # BFS (where each iteration is time t)
        # 'wait' until threshold crosses -> 
        # infinite distances means all (i,j)s are accessible
        # frontier
        from heapq import heappush, heappop
        frontier = [ (grid[0][0],start) ]
        searching = True
        t = 0
        directions = [ [-1,0],[1,0],[0,1],[0,-1]    ]
        visited = set()
        t = 0
        while frontier:
            # process all the frontier elements simultaenously
            print('current iter',t,frontier[0][0])
            while frontier and frontier[0][0] <= t:
                elevation, coord = heappop(frontier)
                i,j = coord
                if (i,j) in visited: continue
                if (i,j) == end: return t
                print(i,j,elevation,t)
                visited.add((i,j))

                for dx, dy in directions:
                    new_i , new_j = i + dx, j + dy
                    if new_i not in range(n): continue
                    if new_j not in range(n): continue
                    if (new_i, new_j) in visited: continue
                    print(( grid[new_i][new_j], (new_i,new_j) ))
                    heappush(frontier,( grid[new_i][new_j], (new_i,new_j) ) )
            t += 1
        return t

