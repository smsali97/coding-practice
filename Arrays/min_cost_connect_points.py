class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1,p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1-x2) + abs(y1-y2)

        from collections import defaultdict
        from heapq import heappush, heappop
        adj = defaultdict(list)
        for p1 in points:
            for p2 in points:
                if p1 == p2: continue
                adj[tuple(p1)].append((tuple(p2),manhattan(p1,p2)))
                adj[tuple(p2)].append((tuple(p1),manhattan(p1,p2)))
        
        frontier = [[0,tuple(points[0])]] # cost,idx
        min_cost = 0
        visited = set()
        N = points
        while len(visited) < len(N):
            cost, point = heappop(frontier)
            if point in visited: continue # because we will have duplicates
            min_cost += cost
            visited.add(point)
            for nei, neiCost in adj[point]:
                if nei in visited: continue
                heappush(frontier,[neiCost,nei])
        return min_cost





