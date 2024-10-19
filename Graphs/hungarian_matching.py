class HungarianAlgorithm:
    def init(self, grid):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])


    def maximumMatching(self):
        match = [-1] * self.n

        def dfs(u):
            for v in range(self.n):
                if self.grid[u][v] and not visited[v]:
                    visited[v] = True
                    if match[v] == -1 or dfs(match[v]):
                        match[v] = u
                        return True
            return False

        result = 0
        for i in range(self.m):
            visited = [False] * self.n
            if dfs(i):
                result += 1
        return result


grid1 = [[1,1,1],
[1,0,1],
[0,0,1]]


grid2 = [[1,0,1,0],
[1,0,0,0],
[0,0,1,0],
[1,1,1,0]]


hungarian1 = HungarianAlgorithm(grid1)
print(hungarian1.maximumMatching()) # Output: 3


hungarian2 = HungarianAlgorithm(grid2)
print(hungarian2.maximumMatching()) # Output: 3