class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        m, n = len(maze), len(maze[0])
        def out_of_bounds(i,j): return i not in range(m) or j not in range(n)
        def in_exit_border(i,j): return (i == m - 1 or j == n - 1 or i == 0 or j == 0) and (i,j) != (entrance[0],entrance[1])


        def bfs(entrance):
            from collections import deque
            q = deque( [ ( entrance[0],entrance[1],0) ] )
            steps = 0
            visited = set()
            while q:
                r, c, steps = q.popleft()
                maze[r][c] = '+'  # Mark as visited AFTER dequeuing
                if in_exit_border(r,c):
                    return steps
                for dx, dy in directions:
                    new_r, new_c = r + dx, c + dy
                    if out_of_bounds(new_r,new_c): continue
                    if (new_r,new_c) in visited: continue
                    if maze[new_r][new_c] == '+': continue
                    maze[new_r][new_c] = '+'
                    q.append((new_r,new_c,steps+1))            
            return -1
        return bfs(entrance)




