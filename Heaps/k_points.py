class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p1,p2):
            # no need for square root as we dont care about the actual answer
            return (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1])
        def distance_to_origin(p1):
            return distance(p1,[0,0])
        
        if not points: return []
        from heapq import heappop, heapify
        heap = [ (distance_to_origin(points[i]), i)  for i in range(len(points)) ]
        heapify(heap)
        return [ points[ heappop(heap)[1] ]  for _ in range(k) ]
