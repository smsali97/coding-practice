import heapq

class Solution:
    def lastStoneWeight(self, stones: list) -> int:
        
        stones = [-1*stone for stone in stones]
        heapq.heapify(stones)
       
        while len(stones) > 1:
            print(stones)
            s1 = -1* heapq.heappop(stones) 
            s2 = -1*heapq.heappop(stones)
            
            x = min(s1,s2)
            y = max(s1,s2)
            
            if x != y:
                heapq.heappush(stones,-1*(y-x))
        if len(stones) < 1: return 0
        return -1*heapq.heappop(stones)
            
            
        